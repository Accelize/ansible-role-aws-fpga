import os
from os.path import join
from itertools import product

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_aws_fpga_runtime_installed(host):
    """
    Test that AWS FPGA runtime libraries are installed.
    """
    assert any(host.file(join(join(*path), 'libfpga_mgmt.so')).exists
               for path in product(('/usr/local/', '/usr/'), ('lib', 'lib64')))
