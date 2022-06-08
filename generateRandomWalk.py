import random, bpy

def randomWalk(x,y,z,count,origin,prevMesh):
    #Create and name new cube
    randomSizeX = random.randint(1,3)
    randomSizeY = random.randint(1,3)
    randomSizeZ = random.randint(1,3)
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(randomSizeX, randomSizeY, randomSizeZ))
    currentMesh = 'AkuObject' + str(random.randrange(99999))
    bpy.context.active_object.name = currentMesh
    #Begin boolean modifier for original object
    if(prevMesh!=None):
        print(prevMesh,currentMesh)
        #create the boolean and select the previous mesh
        bpy.ops.object.modifier_add(type='BOOLEAN')
        #bpy.context.object.modifiers["Boolean"].operation = random.choice(('UNION','UNION','UNION','DIFFERENCE'))
        bpy.context.object.modifiers["Boolean"].operation = 'UNION'
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
    #determine new distance based on size of object
    
    
    x += random.uniform(-1 * randomSizeX/2, randomSizeX/2)
    y += random.uniform(-1 * randomSizeY/2, randomSizeY/2)
    z += random.uniform(-1 * randomSizeZ/2, randomSizeZ/2)
    
    if(count > 0):
        randomWalk(x,y,z,count-1,False,prevMesh)
    else:
        pass

randomWalk(0,0,0,50,True,None)
