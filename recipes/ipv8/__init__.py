from __future__ import absolute_import
from os import getenv
from os.path import join, exists
from sh import mkdir, cp
from pythonforandroid.toolchain import PythonRecipe, current_directory


class LocalIPV8Recipe(PythonRecipe):
    """
    Python-for-Android IPV8 recipe
    """

    url = 'git+https://github.com/Tribler/py-ipv8.git'

    depends = ['tlswitness', 'apsw', 'cryptography', 'libsodium', 'netifaces',
               'python2', 'setuptools', 'twisted', 'lib2to3', 'libnacl'
              ]

    patches = ['no_tunnel_trustchain.patch', 'tlswitness.patch']

    python_depends = ['hyperlink', 'pysqlite3', 'decorator', 'libnacl', 'pyasn1', 'six']

    site_packages_name = 'ipv8'

    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(LocalIPV8Recipe, self).postbuild_arch(arch)

        # Install twistd plugins
        cp('-rf', join(self.get_build_dir(arch.arch), 'twisted'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))
        
        # Copy ipv8_service.py
        cp('-rf', join(self.get_build_dir(arch.arch), 'ipv8_service.py'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))

recipe = LocalIPV8Recipe()
