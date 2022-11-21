# -*- encoding=utf8 -*-
__author__ = "PAICS"

from airtest.cli.parser import cli_setup
from airtest.core.api import auto_setup


def launch():

    if not cli_setup():
        auto_setup(__file__, logdir=False, devices=["Windows:///", ])
        # auto_setup(__file__, logdir=False, devices=["Windows:///",],
                   # project_root="I:/bd/AirtestIDE-win-1.2.13/autopaics/untitled.air")