AWS FPGA Ansible Role
=====================

This Ansible role install the [AWS FPGA](https://github.com/aws/aws-fpga)
runtime libraries and utilities that are required to run FPGA devices based
application on AWS F1 instances.

Requirements
------------

An AWS F1 instance is required as target host for this role.

The role requires to be run as root on the target host.

Role Variables
--------------

* **aws_fpga_allow_non_root**: If `true`, allow FPGA devices access to users in
  the group specified by *aws_fpga_sdk_group*. Default to `false`.
* **aws_fpga_sdk_group**: Name of the group of users that can access to FPGA
  devices. Default to `fpgauser`. No effect if *aws_fpga_allow_non_root* is
  `false`.
* **aws_fpga_sdk_override_group**: If true, do not raise error if the group
  specified by *aws_fpga_sdk_group* already exists. Default to `false`.
  No effect if *aws_fpga_allow_non_root* is `false`.
* **fpga_driver**: FPGA driver name. If specified, install and enable the
  specified Linux kernel driver. See
  [AWS FPGA linux kernel drivers](https://github.com/aws/aws-fpga/tree/master/sdk/linux_kernel_drivers)
  for the list of available drivers.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
  become: true  
  roles:
     - role: accelize.aws_fpga
       vars:
         aws_fpga_allow_non_root: true
```

Dependencies
------------

None.

License
-------

Apache 2.0

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
