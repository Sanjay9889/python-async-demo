"""
Unit Tests
"""
# -*- coding: utf-8 -*-
"""
    Path hack for python 3
"""
import sys
from pathlib import Path

print(str(Path(__file__).resolve().parent.parent) + "/ihs_markit_polk_snowflake/")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent) + "/ihs_markit_polk_snowflake/")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent) + "/tests/")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve()))
