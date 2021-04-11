"""Constants module."""
# Copyright 2021 The dt-web3 Authors
# SPDX-License-Identifier: LGPL-2.1-only

class Role:
    ROLE_ADMIN = 100
    ROLE_ENTERPRISE = 101
    ROLE_PROVIDER = 102


class Operation:
    MODIFY_ADMIN = 200
    MODIFY_ENTERPRISE = 201
    MODIFY_PROVIDER = 202
    MODIFY_OP = 203
    MODIFY_ASSET = 204
    MODIFY_AUTHORIZE = 205
    MODIFY_TASK = 206


class ErrorCode:
    SUCCESS = 0
    ERROR_NO_PERMISSION = 10000
    ROLE_EXISTS = 1001
    ENTERPRISE_EXISTS = 2001
    ENTERPRISE_NOT_EXISTS = 2002
    PROVIDER_EXISTS = 2003
    PROVIDER_NOT_EXISTS = 2004
    TEMPLATE_EXISTS = 3001
    TEMPLATE_NOT_EXISTS = 3002
    DT_EXISTS = 4001
    DT_NOT_EXISTS = 4002
    CDT_EXISTS = 4003
    CDT_NOT_EXISTS = 4004
    DT_GRATED = 4005
    DT_NOT_GRATED = 4006
