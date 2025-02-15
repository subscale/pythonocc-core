/*
##Copyright 2008-2014 Thomas Paviot (tpaviot@gmail.com)
##
##This file is part of pythonOCC.
##
##pythonOCC is free software: you can redistribute it and/or modify
##it under the terms of the GNU Lesser General Public License as published by
##the Free Software Foundation, either version 3 of the License, or
##(at your option) any later version.
##
##pythonOCC is distributed in the hope that it will be useful,
##but WITHOUT ANY WARRANTY; without even the implied warranty of
##MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##GNU General Public License for more details.
##
##You should have received a copy of the GNU Lesser General Public License
##along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/

#if !defined __OCC3d_Renderer__
#define __OCC3d_Renderer__

#ifdef WNT
  #include <windows.h>
  #include <WNT_WClass.hxx>
  #include <WNT_Window.hxx>
#elif defined(__APPLE__) && !defined(MACOSX_USE_GLX)
  #include <Cocoa_Window.hxx>
#else
  #include <Xw_Window.hxx>
#endif

#include <Aspect_Handle.hxx>
#include <AIS_InteractiveContext.hxx>
#include <BRepPrimAPI_MakeBox.hxx>
#include <V3d_Viewer.hxx>
#include <V3d_View.hxx>
#include <AIS_Shape.hxx>
#include <Graphic3d_Camera.hxx>
#include <Graphic3d_RenderingParams.hxx>
#include <Graphic3d_RenderingMode.hxx>
#include <Graphic3d_StereoMode.hxx>
#include <Graphic3d_Mat4.hxx>
#include <Graphic3d_Vec4.hxx>
#include <OpenGl_GraphicDriver.hxx>
#include <Aspect_DisplayConnection.hxx>

#include <cstdlib>
  

class Display3d 
{	
public:
	Standard_EXPORT Display3d();
	Standard_EXPORT virtual ~Display3d();
	Standard_EXPORT void Init(long window_handle);
  Standard_EXPORT void SetAnaglyphMode(int mode);
  Standard_EXPORT void SetNbMsaaSample(int nb);
  Standard_EXPORT void ChangeRenderingParams(int Method,
                                             Standard_Integer        RaytracingDepth,
                                             Standard_Boolean        IsShadowEnabled,
                                             Standard_Boolean        IsReflectionEnabled,
                                             Standard_Boolean        IsAntialiasingEnabled,
                                             Standard_Boolean        IsTransparentShadowEnabled,
                                             int    StereoMode,
                                             int AnaglyphFilter,
                                             Standard_Boolean        ToReverseStereo);
  Standard_EXPORT void EnableVBO();
  Standard_EXPORT void DisableVBO();
  Standard_EXPORT Handle_V3d_View& GetView() {return myV3dView;};
	Standard_EXPORT Handle_V3d_Viewer& GetViewer() {return myV3dViewer;};
  Standard_EXPORT Handle_Graphic3d_Camera& GetCamera() {return myGraphic3dCamera;};
	Standard_EXPORT Handle_AIS_InteractiveContext& GetContext() {return myAISContext;};
  Standard_EXPORT Handle_Graphic3d_StructureManager& GetStructureManager() {return myGraphic3dStructureManager;};
	Standard_EXPORT void Test();
  Standard_EXPORT void GlInfo();

  Standard_EXPORT bool IsOffscreen();
  Standard_EXPORT bool InitOffscreen(int size_x, int size_y);
  Standard_EXPORT bool SetSize(int size_x, int size_y);
  Standard_EXPORT bool GetSize(int &size_x, int &size_y);
  Standard_EXPORT bool GetImageData(int width,
                                    int height,
                                    const char* &data,
                                    size_t &size,
                                    const Graphic3d_BufferType& theBufferType = Graphic3d_BT_RGB);

protected:
   Handle_AIS_InteractiveContext myAISContext;
   Handle_V3d_Viewer myV3dViewer;
   Handle_V3d_View myV3dView;
   Handle_Graphic3d_Camera myGraphic3dCamera;
   Handle_Graphic3d_StructureManager myGraphic3dStructureManager;

   int mySizeX;
   int mySizeY;
   bool myIsOffscreen;

   #ifdef WNT
     Handle_WNT_Window myWindow;
   #elif defined(__APPLE__) && !defined(MACOSX_USE_GLX)
     Handle_Cocoa_Window myWindow;
   #else
     Handle_Xw_Window myWindow;
   #endif
};

#endif
