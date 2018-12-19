from __future__ import absolute_import
from os.path import join, dirname
from sh import cp
from pythonforandroid.toolchain import PythonRecipe


class TLSWitnessRecipe(PythonRecipe):
    """
    Python-for-Android TLSWitness recipe
    """

    version = '0.1.dev0'
    url = 'http://localhost/TLSWitness-{version}.tar.gz'
    depends = ['python2', 'twisted']
    patches = []
    python_depends = ['treq', 'oscrypto', 'ecdsa', 'tlslite-ng', 'urllib3', 'chardet', 'certifi', 'requests', 'certvalidator']
    site_packages_name = 'tlswitness'
    call_hostpython_via_targetpython = False

    def postbuild_arch(self, arch):
        super(TLSWitnessRecipe, self).postbuild_arch(arch)

        # Ensure the anydbm module works (required by tlslite-ng)
        cp('-rf', join(self.ctx.get_python_install_dir(), 'lib', 'python2.7', 'anydbm.py'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))
        cp('-rf', join(self.ctx.get_python_install_dir(), 'lib', 'python2.7', 'whichdb.py'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))
        cp('-rf', join(self.ctx.get_python_install_dir(), 'lib', 'python2.7', 'dumbdbm.py'),
           join(self.ctx.get_python_install_dir(), 'lib/python2.7/site-packages'))


recipe = TLSWitnessRecipe()

