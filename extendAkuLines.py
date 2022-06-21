import random, bpy

def extendAkuLines():
    pushOut = random.randrange(1,4)
    pushOutEnd = random.randrange(1,4)
    pushVertical = random.randrange(1,3) * random.choice((-1,1))
    print(pushOut,pushOutEnd,pushVertical)
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(pushOut,0,0)})
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0,0,pushVertical)})
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(pushOutEnd,0,0)})


extendAkuLines()