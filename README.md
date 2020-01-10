:warning: **This role is deprecated and as been merged inside the "accelize.xilinx_xrt" role**

**To handle the backward compatibility, this role now act as a redirection**

AWS FPGA Ansible Role
=====================

This Ansible role install the [AWS FPGA](https://github.com/aws/aws-fpga) runtime libraries and utilities that are required to run FPGA devices based application on AWS F1 instances.

Requirements
------------

See **accelize.xilinx_xrt** documentation. 

Role Variables
--------------

See **accelize.xilinx_xrt** documentation. 

Following variables that are not in **accelize.xilinx_xrt** still exists for compatibility:

* **aws_fpga_xrt**: If `true`, also install Xilinx XRT.
  Default to `true`.
* **aws_fpga_driver**: Ignored. The XOCL diver is installed with the XRT package.

Example Playbook
----------------

See **accelize.xilinx_xrt** documentation. 

Dependencies
------------

- **accelize.xilinx_xrt**.

License
-------

Copyright Accelize 2019, Apache 2.0

Installed components licences:

* [Xilinx XRT license](https://github.com/Xilinx/XRT/blob/master/LICENSE)
* [AWS FPGA license](https://github.com/aws/aws-fpga/blob/master/LICENSE.txt)

*This Ansible role is not endorsed or affiliated by Xilinx or AWS.*

Author Information
------------------

This role is provided by [Accelize](https://www.accelize.com).
