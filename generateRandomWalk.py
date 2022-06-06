import random, bpy

def randomWalk(x,y,z,count,origin,prevMesh):
    #Create and name new cube
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))
    currentMesh = 'AkuObject' + str(random.randrange(999))
    bpy.context.active_object.name = currentMesh
    #Begin boolean modifier for original object
    if(prevMesh!=None):
        print(prevMesh,currentMesh)
        #create the boolean and select the previous mesh
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].operation = random.choice(('UNION','DIFFERENCE'))
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[prevMesh]
        bpy.ops.object.modifier_apply(modifier="Boolean")
        bpy.data.objects[prevMesh].select_set(True)
        bpy.data.objects[currentMesh].select_set(False)
        bpy.ops.object.delete()
        bpy.data.objects[currentMesh].select_set(True)
        prevMesh = bpy.context.active_object.name
    else:
         prevMesh = bpy.context.active_object.name
         
    #New cooridinates for walk
    x += random.uniform(-2,2)
    y += random.uniform(-2,2)
    z += random.uniform(-2,2)
    
    if(count > 0):
        randomWalk(x,y,z,count-1,False,prevMesh)
    else:
        pass

randomWalk(0,0,0,50,True,None)
