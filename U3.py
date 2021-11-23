# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 11:00:19 2021

@author: DELL
"""
import vtk

############# show a cone  #########
cone = vtk.vtkConeSource()

coneMapper = vtk.vtkDataSetMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

coneRen = vtk.vtkRenderer()
coneRen.AddActor(coneActor)
coneRen.SetBackground(0.1,0.2,0.4)
coneWin = vtk.vtkRenderWindow()
coneWin.AddRenderer(coneRen)
coneWin.Render()


iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(coneWin)
iren.Initialize()
iren.Start()

#%%
##########show both together ###############

cone = vtk.vtkConeSource()

coneMapper = vtk.vtkDataSetMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

coneRen1 = vtk.vtkRenderer()
coneRen1.AddActor(coneActor)
coneRen1.SetBackground(0.3,0.6,0.3)
coneRen1.SetViewport(0.0,0.0,0.5,1.0) #x, y, width, height



coneRen2 = vtk.vtkRenderer()
coneRen2.AddActor(coneActor)
coneRen2.SetBackground(0.2,0.3,0.5)
coneRen2.SetViewport(0.5,0.0,1.0,1.0)

coneWin = vtk.vtkRenderWindow()
coneWin.AddRenderer(coneRen1)
coneWin.AddRenderer(coneRen2)
coneWin.SetSize(600,300)

#coneWin.Render()

#coneRen1.GetActiveCamera().Azimuth(90)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(coneWin)
iren.Initialize()
iren.Start()

#%%

cone = vtk.vtkConeSource()

coneMapper = vtk.vtkDataSetMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

####### add features ###############

coneActor.GetProperty().SetColor(0.2,0.63,0.79)
coneActor.GetProperty().SetDiffuse(0.7)
coneActor.GetProperty().SetSpecular(0.4)
coneActor.GetProperty().SetSpecularPower(20)

propertys = vtk.vtkProperty()
propertys.SetColor(1.0,0.3882,0.2784)
propertys.SetDiffuse(0.7)
propertys.SetSpecular(0.4)
propertys.SetSpecularPower(20)
#####################################



####### create the second actor and add the same features with diiferent color ###############
coneActor2 = vtk.vtkActor()
coneActor2.SetMapper(coneMapper)

#coneActor2.GetProperty().SetColor(0.2,0.63,0.79)
coneActor2.SetProperty(propertys)
coneActor2.SetPosition(1,2,0.5) #affects the trans matrix

######## show in the same figure #################
coneRen1 = vtk.vtkRenderer()
coneRen1.AddActor(coneActor)
coneRen1.AddActor(coneActor2)
coneRen1.SetBackground(0.1,0.2,0.4)



coneWin = vtk.vtkRenderWindow()
coneWin.AddRenderer(coneRen1)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(coneWin)
iren.Initialize()
iren.Start()

#%%
############# transformations ####################

cone = vtk.vtkConeSource()

coneMapper = vtk.vtkDataSetMapper()
coneMapper.SetInputConnection(cone.GetOutputPort())
coneActor = vtk.vtkActor()
coneActor.SetMapper(coneMapper)

### using vtkTransform ###
# myTrans = vtk.vtkTransform()
# myTrans.Translate(0,0,5)
# myTrans.RotateZ(45)
# coneActor.SetUserMatrix(myTrans.GetMatrix())  ## GetMatrix ---> get world transfer matrix
                                                ## SetUserMatrix -----> set user transfer matrix

#### using actor #########

coneActor.SetOrigin(0,0,-5)
coneActor.RotateZ(45)
coneActor.SetPosition(0,0,5)


coneRen1 = vtk.vtkRenderer()
coneRen1.AddActor(coneActor)

coneRen1.SetBackground(0.1,0.2,0.4)

coneWin = vtk.vtkRenderWindow()
coneWin.AddRenderer(coneRen1)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(coneWin)
iren.Initialize()
iren.Start()
