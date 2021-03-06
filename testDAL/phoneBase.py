__author__ = 'shikun'
# -*- coding: utf-8 -*-
import os
import subprocess
import re


# 得到手机信息
def get_phone_info(devices):
    l_list = {'release': 'unknown', 'model': 'unknown', 'brand': 'unknown', 'device': 'unknown'}
    cmd = "adb -s " + devices + " shell cat /system/build.prop"
    (output, err) = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     stdin=subprocess.PIPE, shell=True).communicate()
    if output:
        output = output.decode()
        release_match = re.compile("ro.build.version.release=(.+)\s+").search(output)
        model_match = re.compile("ro.product.model=(.+)\s+").search(output)
        brand_match = re.compile("ro.product.brand=(.+)\s+").search(output)
        device_match = re.compile("ro.product.device=(.+)\s+").search(output)
        if release_match:
            l_list["release"] = release_match.group(1).strip()
        if model_match:
            l_list["model"] = model_match.group(1).strip()
        if brand_match:
            l_list["brand"] = brand_match.group(1).strip()
        if device_match:
            l_list["device"] = device_match.group(1).strip()
    return l_list


# 得到最大运行内存
def get_men_total(devices):
    cmd = "adb -s " + devices + " shell cat /proc/meminfo"
    output = os.popen(cmd).read()
    men_total = 0
    if output:
        match = re.compile("MemTotal:\s+(\d+)\skB").search(output)
        if match:
            men_total = int(match.group(1))
    return men_total


# 得到几核cpu
def get_cpu_kel(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    output = os.popen(cmd).read()
    int_cpu = 0
    if output:
        match = re.compile("processor\s*: \d+").findall(output)
        if match:
            int_cpu = len(match)
    return str(int_cpu) + "核"


# 得到手机分辨率
def get_app_pix(devices):
    try:
        result = os.popen("adb -s " + devices + " shell wm size", "r").read()
        match = re.compile("Physical size: (\d+x\d+)\s+").search(result)
        if match:
            return match.group(1)
    except:
        pass
    return "Unknown"


def remove_file(device, file):
    cmd = "adb -s " + device + " shell rm " + file
    os.popen(cmd).readlines()


def read_file(device, file):
    cmd = "adb -s " + device + " shell cat " + file
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    output = output.decode()
    if "No such file or directory" in output:
        return ""
    return output


if __name__=="__main__":
    print(get_phone_info("TA09003E57"))
    print(get_cpu_kel("TA09003E57"))
    print(get_men_total("TA09003E57"))
    print(get_app_pix("TA09003E57"))
