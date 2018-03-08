#!/usr/bin/env python
import angr
import claripy
p = angr.Project("arg_string")
arg1 = claripy.BVS("arg1", 8*2)
st = p.factory.entry_state(args=["a.out", arg1])
sm = p.factory.simulation_manager(st)
sm.explore(find=(0x4006b9,))
found = sm.found[0]
print found.state.se.eval(arg1, cast_to=str)

