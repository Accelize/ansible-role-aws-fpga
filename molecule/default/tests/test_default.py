import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fpga_mgnt_installed(host):
    """
    Test that FPGA management libraries and utilities are installed.
    """
    from os.path import join
    from itertools import product

    usr = ('/usr/local/', '/usr/')
    lib_dirs = ('lib', 'lib64')
    bin_dirs = 'bin',

    def exists(name, *base_paths):
        """
        Check if file installed in at least one directory.

        Args:
            name (str): relative path to file.
            base_paths (tuple of str): base paths where file can be installed.

        Returns:
            bool: True if installed
        """
        return any(host.file(join(join(*path), name)).exists
                   for path in product(*base_paths))

    # Libraries
    for library in ('libfpga_mgmt.so',
                    'libfpga_mgmt.so.1',
                    'libfpga_mgmt.so.1.0.0'):
        assert exists(library, usr, lib_dirs), library

    # Minimal utilities
    for utility in ('fpga-describe-local-image',
                    'fpga-load-local-image',
                    'fpga-clear-local-image'):
        assert exists(utility, usr, bin_dirs), utility
