#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 vagrant 
#
# Distributed under terms of the MIT license.
import sys
import os

lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
apps_dir = os.path.join(os.path.dirname(__file__), 'apps')
sys.path.insert(0, lib_dir)
sys.path.insert(0, apps_dir)


