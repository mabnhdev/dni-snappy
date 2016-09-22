import os
import shutil
import glob
import logging
import snapcraft.plugins.kernel

logger = logging.getLogger(__name__)

class XKernelPlugin(snapcraft.plugins.kernel.KernelPlugin):

    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['kernel-patches'] = {
            'type': 'array',
            'uniqueItems': True,
            'items': {
                'type': 'string',
            },
            'default': [],
        }
        schema['properties']['kernel-custom-modules'] = {
            'type': 'array',
            'uniqueItems': True,
            'items': {
                'type': 'string',
            },
            'default': [],
        }
        schema['pull-properties'].extend(['kernel-patches'])
        schema['build-properties'].extend(['kernel-custom-modules'])

        return schema

    def pull(self):
        super().pull()
        for patch in self.options.kernel_patches:
            pfile = os.path.join(os.getcwd(), patch)
            logger.info('Patching kernel with ' +  pfile)
            self.run(['patch', '-d', self.sourcedir, '-p1', '-i', pfile])

    def build(self):
        super().build()
        if self.options.kernel_custom_modules:
            print ()
            print ('Build the following custom modules using ' + self.sourcedir)
            print ()
            for module in self.options.kernel_custom_modules:
                print ('\t' + module)
            print ()
            input("Press any key when modules have been built...")
            print ()
            dest = os.path.dirname(glob.glob(os.path.join(self.installdir, 'lib/modules/*/kernel'))[0])
            for mod in self.options.kernel_custom_modules:
                shutil.copy(mod, dest)
            self.run(['depmod', '-b', self.installdir, os.path.basename(dest)])

        # There is currently a bug reported that the kernel build uses the
        # wrong name for the kernel object.  As a workaround, rename the kernel
        # object to the correct name.
        # Fixed in snapcraft 2.16.
        vm = os.path.join(self.installdir, 'vmlinuz')
        img = os.path.join(self.installdir, 'kernel.img')
        if (not os.path.isfile(img)):
            os.rename(vm, img)
