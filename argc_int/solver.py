#!/usr/bin/env python
import angr
import claripy
p = angr.Project("argc_int")
argc = claripy.BVS("argc", 8)
st = p.factory.call_state(0x40063a, argc)
sm = p.factory.simulation_manager(st)
sm.explore(find=(0x40064f,))
found = sm.found[0]
print found.state.se.eval(argc)

