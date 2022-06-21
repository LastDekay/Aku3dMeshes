import bpy, random

def startGen():
    startPos = random.randrange(5)
    bpy.ops.mesh.primitive_vert_add()
    bpy.ops.transform.translate(value=(0, 0, startPos), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    for x in range(random.randint(2,5)):
        extrudeLine()
    bpy.ops.object.modifier_add(type='SCREW')
    bpy.context.object.modifiers["Screw"].axis = 'X'
    bpy.context.object.modifiers["Screw"].use_smooth_shade = False
    bpy.ops.object.modifier_add(type='SOLIDIFY')

    
def extrudeLine():
    pushOut = random.randrange(1,4)
    pushOutEnd = random.randrange(1,4)
    pushVertical = random.randrange(1,3) * random.choice((-1,1))
    print(pushOut,pushOutEnd,pushVertical)
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(pushOut,0,0)})
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0,0,pushVertical)})
    bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(pushOutEnd,0,0)})
    

startGen()


#bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0,1,0)})

