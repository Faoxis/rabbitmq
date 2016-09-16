#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
a = OrderedDict()
a['one'] = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
a['two'] = OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
a['three'] = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
a['four'] = OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
a['five'] = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
a['six'] = OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

print type(a)
for key, value in a.items():
    print str(key) + ":  " + str(value)