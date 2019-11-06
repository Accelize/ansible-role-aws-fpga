[![Build Status](https://travis-ci.org/Accelize/ansible-role-aws-fpga.svg?branch=master)](https://travis-ci.org/Accelize/ansible-role-aws-fpga)

AWS FPGA Ansible Role
=====================

This Ansible role install the [AWS FPGA](https://github.com/aws/aws-fpga) runtime libraries and utilities that are required to run FPGA devices based application on AWS F1 instances.

Requirements
------------

An AWS F1 instance is required as target host for this role.

The role requires to be run as root on the target host.

CentOS 7 is recommanded since it the only one officially tested by Xilinx/AWS.

**accelize.xilinx_xrt** role if required to install Xilinx XRT on non CentOS 7
systems.

Role Variables
--------------

* **aws_fpga_version**: AWS FPGA version; If not specified, use latest version available.

* **aws_fpga_allow_non_root**: If `true`, allow FPGA devices access to users in the group specified by *aws_fpga_sdk_group*.
  Default to `false`.
* **aws_fpga_sdk_group**: Name of the group of users that can access to FPGA devices.
  Default to `fpgauser`.
  No effect if *aws_fpga_allow_non_root* is `false`.
* **aws_fpga_sdk_override_group**: If true, do not raise error if the group specified by *aws_fpga_sdk_group* already exists.
  Default to `false`. No effect if *aws_fpga_allow_non_root* is `false`.
* **aws_fpga_src_install**: If specified, install AWS FPGA sources in the specified directory.

* **aws_fpga_xrt**: If `true`, also install Xilinx XRT.
  Default to `true`.
* **xilinx_xrt_version**: If *aws_fpga_xrt* is `true`, Xilinx XRT version to install.
  Default to `2019.1`.
* **xilinx_xrt_ensure_compatible_kernel**: If `true`, ensure the Linux kernel installed is compatible. Default to `true`.

* **aws_fpga_driver**: FPGA driver name. If specified, install and enable the specified Linux kernel driver.
  See [AWS FPGA linux kernel drivers](https://github.com/aws/aws-fpga/tree/master/sdk/linux_kernel_drivers) for the list of available drivers.
  If *aws_fpga_xrt* is `true`, the XOCl driver shipped with XRT is installed.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.aws_fpga
```

Dependencies
------------

None.

License
-------

Apache 2.0

This Ansible role is not endorsed or affiliated by AWS or Xilinx.

* [AWS FPGA license](https://github.com/aws/aws-fpga/blob/master/LICENSE.txt)
* [Xilinx XRT license](https://github.com/Xilinx/XRT/blob/master/LICENSE)

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
