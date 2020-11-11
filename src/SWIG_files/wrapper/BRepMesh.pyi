from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.IMeshTools import *
from OCC.Core.Message import *
from OCC.Core.gp import *
from OCC.Core.TopAbs import *
from OCC.Core.TopoDS import *
from OCC.Core.GeomAbs import *
from OCC.Core.TCollection import *
from OCC.Core.TColStd import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.Adaptor3d import *
from OCC.Core.Poly import *
from OCC.Core.Bnd import *
from OCC.Core.TopLoc import *
from OCC.Core.Geom2d import *
from OCC.Core.Geom import *
from OCC.Core.IMeshData import *


class BRepMesh_FactoryError(IntEnum):
	BRepMesh_FE_NOERROR: int = ...
	BRepMesh_FE_LIBRARYNOTFOUND: int = ...
	BRepMesh_FE_FUNCTIONNOTFOUND: int = ...
	BRepMesh_FE_CANNOTCREATEALGO: int = ...
BRepMesh_FE_NOERROR = BRepMesh_FactoryError.BRepMesh_FE_NOERROR
BRepMesh_FE_LIBRARYNOTFOUND = BRepMesh_FactoryError.BRepMesh_FE_LIBRARYNOTFOUND
BRepMesh_FE_FUNCTIONNOTFOUND = BRepMesh_FactoryError.BRepMesh_FE_FUNCTIONNOTFOUND
BRepMesh_FE_CANNOTCREATEALGO = BRepMesh_FactoryError.BRepMesh_FE_CANNOTCREATEALGO

class BRepMesh_DegreeOfFreedom(IntEnum):
	BRepMesh_Free: int = ...
	BRepMesh_InVolume: int = ...
	BRepMesh_OnSurface: int = ...
	BRepMesh_OnCurve: int = ...
	BRepMesh_Fixed: int = ...
	BRepMesh_Frontier: int = ...
	BRepMesh_Deleted: int = ...
BRepMesh_Free = BRepMesh_DegreeOfFreedom.BRepMesh_Free
BRepMesh_InVolume = BRepMesh_DegreeOfFreedom.BRepMesh_InVolume
BRepMesh_OnSurface = BRepMesh_DegreeOfFreedom.BRepMesh_OnSurface
BRepMesh_OnCurve = BRepMesh_DegreeOfFreedom.BRepMesh_OnCurve
BRepMesh_Fixed = BRepMesh_DegreeOfFreedom.BRepMesh_Fixed
BRepMesh_Frontier = BRepMesh_DegreeOfFreedom.BRepMesh_Frontier
BRepMesh_Deleted = BRepMesh_DegreeOfFreedom.BRepMesh_Deleted

class BRepMesh_BaseMeshAlgo(IMeshTools_MeshAlgo):
	pass

class BRepMesh_Circle:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theLocation: gp_XY, theRadius: float) -> None: ...
	def Location(self) -> gp_XY: ...
	def Radius(self) -> float: ...
	def SetLocation(self, theLocation: gp_XY) -> None: ...
	def SetRadius(self, theRadius: float) -> None: ...

class BRepMesh_CircleInspector(NCollection_CellFilter_InspectorXY):
	def __init__(self, theTolerance: float, theReservedSize: int, theAllocator: NCollection_IncAllocator) -> None: ...
	def Bind(self, theIndex: int, theCircle: BRepMesh_Circle) -> None: ...
	def Circle(self, theIndex: int) -> BRepMesh_Circle: ...
	def Circles(self) -> False: ...
	def GetShotCircles(self) -> False: ...
	def Inspect(self, theTargetIndex: int) -> NCollection_CellFilter_Action: ...
	@staticmethod
	def IsEqual(theIndex: int, theTargetIndex: int) -> bool: ...
	def SetPoint(self, thePoint: gp_XY) -> None: ...

class BRepMesh_CircleTool:
	@overload
	def __init__(self, theAllocator: NCollection_IncAllocator) -> None: ...
	@overload
	def __init__(self, theReservedSize: int, theAllocator: NCollection_IncAllocator) -> None: ...
	@overload
	def Bind(self, theIndex: int, theCircle: gp_Circ2d) -> None: ...
	@overload
	def Bind(self, theIndex: int, thePoint1: gp_XY, thePoint2: gp_XY, thePoint3: gp_XY) -> bool: ...
	def Delete(self, theIndex: int) -> None: ...
	def IsEmpty(self) -> bool: ...
	@staticmethod
	def MakeCircle(thePoint1: gp_XY, thePoint2: gp_XY, thePoint3: gp_XY, theLocation: gp_XY) -> Tuple[bool, float]: ...
	def MocBind(self, theIndex: int) -> None: ...
	def Select(self, thePoint: gp_XY) -> False: ...
	@overload
	def SetCellSize(self, theSize: float) -> None: ...
	@overload
	def SetCellSize(self, theSizeX: float, theSizeY: float) -> None: ...
	def SetMinMaxSize(self, theMin: gp_XY, theMax: gp_XY) -> None: ...

class BRepMesh_Classifier(Standard_Transient):
	def __init__(self) -> None: ...
	def Perform(self, thePoint: gp_Pnt2d) -> TopAbs_State: ...

class BRepMesh_Context(IMeshTools_Context):
	def __init__(self, theMeshType: Optional[IMeshTools_MeshAlgoType] = IMeshTools_MeshAlgoType_DEFAULT) -> None: ...

class BRepMesh_CurveTessellator(IMeshTools_CurveTessellator):
	def PointsNb(self) -> int: ...
	def Value(self, theIndex: int, thePoint: gp_Pnt) -> Tuple[bool, float]: ...

class BRepMesh_DataStructureOfDelaun(Standard_Transient):
	def __init__(self, theAllocator: NCollection_IncAllocator, theReservedNodeSize: Optional[int] = 100) -> None: ...
	def AddElement(self, theElement: BRepMesh_Triangle) -> int: ...
	def AddLink(self, theLink: BRepMesh_Edge) -> int: ...
	def AddNode(self, theNode: BRepMesh_Vertex, isForceAdd: Optional[bool] = False) -> int: ...
	def Allocator(self) -> NCollection_IncAllocator: ...
	def ClearDeleted(self) -> None: ...
	def ClearDomain(self) -> None: ...
	def Data(self) -> BRepMesh_VertexTool: ...
	def Dump(self, theFileNameStr: str) -> None: ...
	def ElementsConnectedTo(self, theLinkIndex: int) -> BRepMesh_PairOfIndex: ...
	def ElementsOfDomain(self) -> False: ...
	def GetElement(self, theIndex: int) -> BRepMesh_Triangle: ...
	def GetLink(self, theIndex: int) -> BRepMesh_Edge: ...
	def GetNode(self, theIndex: int) -> BRepMesh_Vertex: ...
	@overload
	def IndexOf(self, theNode: BRepMesh_Vertex) -> int: ...
	@overload
	def IndexOf(self, theLink: BRepMesh_Edge) -> int: ...
	def LinksConnectedTo(self, theIndex: int) -> False: ...
	def LinksOfDomain(self) -> False: ...
	def NbElements(self) -> int: ...
	def NbLinks(self) -> int: ...
	def NbNodes(self) -> int: ...
	def RemoveElement(self, theIndex: int) -> None: ...
	def RemoveLink(self, theIndex: int, isForce: Optional[bool] = False) -> None: ...
	def RemoveNode(self, theIndex: int, isForce: Optional[bool] = False) -> None: ...
	def SubstituteElement(self, theIndex: int, theNewElement: BRepMesh_Triangle) -> bool: ...
	def SubstituteLink(self, theIndex: int, theNewLink: BRepMesh_Edge) -> bool: ...
	def SubstituteNode(self, theIndex: int, theNewNode: BRepMesh_Vertex) -> bool: ...

class BRepMesh_Deflection(Standard_Transient):
	@staticmethod
	def ComputeAbsoluteDeflection(theShape: TopoDS_Shape, theRelativeDeflection: float, theMaxShapeSize: float) -> float: ...
	@staticmethod
	def IsConsistent(theCurrent: float, theRequired: float, theAllowDecrease: bool, theRatio: Optional[float] = 0.1) -> bool: ...

class BRepMesh_DelabellaMeshAlgoFactory(IMeshTools_MeshAlgoFactory):
	def __init__(self) -> None: ...
	def GetAlgo(self, theSurfaceType: GeomAbs_SurfaceType, theParameters: IMeshTools_Parameters) -> IMeshTools_MeshAlgo: ...

class BRepMesh_Delaun:
	@overload
	def __init__(self, theOldMesh: BRepMesh_DataStructureOfDelaun, theCellsCountU: int, theCellsCountV: int, isFillCircles: bool) -> None: ...
	def Circles(self) -> BRepMesh_CircleTool: ...
	def Contains(self, theTriangleId: int, theVertex: BRepMesh_Vertex, theSqTolerance: float) -> Tuple[bool, int]: ...
	def GetEdge(self, theIndex: int) -> BRepMesh_Edge: ...
	def GetTriangle(self, theIndex: int) -> BRepMesh_Triangle: ...
	def GetVertex(self, theIndex: int) -> BRepMesh_Vertex: ...
	def InitCirclesTool(self, theCellsCountU: int, theCellsCountV: int) -> None: ...
	def RemoveAuxElements(self) -> None: ...
	def RemoveVertex(self, theVertex: BRepMesh_Vertex) -> None: ...
	def Result(self) -> BRepMesh_DataStructureOfDelaun: ...
	def UseEdge(self, theEdge: int) -> bool: ...

class BRepMesh_DiscretFactory:
	def DefaultName(self) -> TCollection_AsciiString: ...
	def Discret(self, theShape: TopoDS_Shape, theLinDeflection: float, theAngDeflection: float) -> BRepMesh_DiscretRoot: ...
	def ErrorStatus(self) -> BRepMesh_FactoryError: ...
	def FunctionName(self) -> TCollection_AsciiString: ...
	@staticmethod
	def Get() -> BRepMesh_DiscretFactory: ...
	def Names(self) -> TColStd_MapOfAsciiString: ...
	def SetDefault(self, theName: TCollection_AsciiString, theFuncName: Optional[TCollection_AsciiString] = "DISCRETALGO") -> bool: ...
	def SetDefaultName(self, theName: TCollection_AsciiString) -> bool: ...
	def SetFunctionName(self, theFuncName: TCollection_AsciiString) -> bool: ...

class BRepMesh_DiscretRoot(Standard_Transient):
	def IsDone(self) -> bool: ...
	def Perform(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	def SetShape(self, theShape: TopoDS_Shape) -> None: ...
	def Shape(self) -> TopoDS_Shape: ...

class BRepMesh_EdgeDiscret(IMeshTools_ModelAlgo):
	def __init__(self) -> None: ...

class BRepMesh_FaceChecker(Standard_Transient):
	def Perform(self) -> bool: ...

class BRepMesh_FaceDiscret(IMeshTools_ModelAlgo):
	def __init__(self, theAlgoFactory: IMeshTools_MeshAlgoFactory) -> None: ...

class BRepMesh_GeomTool:
	@overload
	def __init__(self, theCurve: BRepAdaptor_Curve, theFirstParam: float, theLastParam: float, theLinDeflection: float, theAngDeflection: float, theMinPointsNb: Optional[int] = 2, theMinSize: Optional[float] = precision_Confusion()) -> None: ...
	@overload
	def __init__(self, theSurface: BRepAdaptor_HSurface, theIsoType: GeomAbs_IsoType, theParamIso: float, theFirstParam: float, theLastParam: float, theLinDeflection: float, theAngDeflection: float, theMinPointsNb: Optional[int] = 2, theMinSize: Optional[float] = precision_Confusion()) -> None: ...
	def AddPoint(self, thePoint: gp_Pnt, theParam: float, theIsReplace: Optional[bool] = True) -> int: ...
	@staticmethod
	def CellsCount(theSurface: Adaptor3d_HSurface, theVerticesNb: int, theDeflection: float, theRangeSplitter: BRepMesh_DefaultRangeSplitter) -> False: ...
	def NbPoints(self) -> int: ...
	@staticmethod
	def SquareDeflectionOfSegment(theFirstPoint: gp_Pnt, theLastPoint: gp_Pnt, theMidPoint: gp_Pnt) -> float: ...
	@overload
	def Value(self, theIndex: int, theIsoParam: float, thePoint: gp_Pnt, theUV: gp_Pnt2d) -> Tuple[bool, float]: ...
	@overload
	def Value(self, theIndex: int, theSurface: BRepAdaptor_HSurface, thePoint: gp_Pnt, theUV: gp_Pnt2d) -> Tuple[bool, float]: ...

class BRepMesh_MeshAlgoFactory(IMeshTools_MeshAlgoFactory):
	def __init__(self) -> None: ...
	def GetAlgo(self, theSurfaceType: GeomAbs_SurfaceType, theParameters: IMeshTools_Parameters) -> IMeshTools_MeshAlgo: ...

class BRepMesh_MeshTool(Standard_Transient):
	@overload
	def __init__(self, theStructure: BRepMesh_DataStructureOfDelaun) -> None: ...
	def AddAndLegalizeTriangle(self, thePoint1: int, thePoint2: int, thePoint3: int) -> None: ...
	def AddLink(self, theFirstNode: int, theLastNode: int) -> Tuple[int, bool]: ...
	def CleanFrontierLinks(self) -> None: ...
	@overload
	def EraseFreeLinks(self) -> None: ...
	def EraseItemsConnectedTo(self, theNodeIndex: int) -> None: ...
	def GetStructure(self) -> BRepMesh_DataStructureOfDelaun: ...
	def Legalize(self, theLinkIndex: int) -> None: ...

class BRepMesh_ModelBuilder(IMeshTools_ModelBuilder):
	def __init__(self) -> None: ...

class BRepMesh_ModelHealer(IMeshTools_ModelAlgo):
	def __init__(self) -> None: ...

class BRepMesh_ModelPostProcessor(IMeshTools_ModelAlgo):
	def __init__(self) -> None: ...

class BRepMesh_ModelPreProcessor(IMeshTools_ModelAlgo):
	def __init__(self) -> None: ...

class BRepMesh_OrientedEdge:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theFirstNode: int, theLastNode: int) -> None: ...
	def FirstNode(self) -> int: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def IsEqual(self, theOther: BRepMesh_OrientedEdge) -> bool: ...
	def LastNode(self) -> int: ...

class BRepMesh_PairOfIndex:
	def __init__(self) -> None: ...
	def Append(self, theIndex: int) -> None: ...
	def Clear(self) -> None: ...
	def Extent(self) -> int: ...
	def FirstIndex(self) -> int: ...
	def Index(self, thePairPos: int) -> int: ...
	def IsEmpty(self) -> bool: ...
	def LastIndex(self) -> int: ...
	def Prepend(self, theIndex: int) -> None: ...
	def RemoveIndex(self, thePairPos: int) -> None: ...
	def SetIndex(self, thePairPos: int, theIndex: int) -> None: ...

class BRepMesh_SelectorOfDataStructureOfDelaun(Standard_Transient):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theMesh: BRepMesh_DataStructureOfDelaun) -> None: ...
	def AddNeighbours(self) -> None: ...
	def Elements(self) -> False: ...
	def FrontierLinks(self) -> False: ...
	def Initialize(self, theMesh: BRepMesh_DataStructureOfDelaun) -> None: ...
	def Links(self) -> False: ...
	def NeighboursByEdgeOf(self, theElement: BRepMesh_Triangle) -> None: ...
	@overload
	def NeighboursOf(self, theNode: BRepMesh_Vertex) -> None: ...
	@overload
	def NeighboursOf(self, theLink: BRepMesh_Edge) -> None: ...
	@overload
	def NeighboursOf(self, theElement: BRepMesh_Triangle) -> None: ...
	def NeighboursOfElement(self, theElementIndex: int) -> None: ...
	def NeighboursOfLink(self, theLinkIndex: int) -> None: ...
	def NeighboursOfNode(self, theNodeIndex: int) -> None: ...
	def Nodes(self) -> False: ...

class BRepMesh_ShapeTool(Standard_Transient):
	@staticmethod
	def AddInFace(theFace: TopoDS_Face, theTriangulation: Poly_Triangulation) -> None: ...
	@staticmethod
	def BoxMaxDimension(theBox: Bnd_Box) -> float: ...
	@staticmethod
	def MaxFaceTolerance(theFace: TopoDS_Face) -> float: ...
	@overload
	@staticmethod
	def NullifyEdge(theEdge: TopoDS_Edge, theTriangulation: Poly_Triangulation, theLocation: TopLoc_Location) -> None: ...
	@overload
	@staticmethod
	def NullifyEdge(theEdge: TopoDS_Edge, theLocation: TopLoc_Location) -> None: ...
	@staticmethod
	def NullifyFace(theFace: TopoDS_Face) -> None: ...
	@overload
	@staticmethod
	def Range(theEdge: TopoDS_Edge, theFace: TopoDS_Face, thePCurve: Geom2d_Curve, isConsiderOrientation: Optional[bool] = False) -> Tuple[bool, float, float]: ...
	@overload
	@staticmethod
	def Range(theEdge: TopoDS_Edge, theCurve: Geom_Curve, isConsiderOrientation: Optional[bool] = False) -> Tuple[bool, float, float]: ...
	@staticmethod
	def UVPoints(theEdge: TopoDS_Edge, theFace: TopoDS_Face, theFirstPoint2d: gp_Pnt2d, theLastPoint2d: gp_Pnt2d, isConsiderOrientation: Optional[bool] = False) -> bool: ...
	@overload
	@staticmethod
	def UpdateEdge(theEdge: TopoDS_Edge, thePolygon: Poly_PolygonOnTriangulation, theTriangulation: Poly_Triangulation, theLocation: TopLoc_Location) -> None: ...
	@overload
	@staticmethod
	def UpdateEdge(theEdge: TopoDS_Edge, thePolygon: Poly_Polygon3D) -> None: ...
	@overload
	@staticmethod
	def UpdateEdge(theEdge: TopoDS_Edge, thePolygon1: Poly_PolygonOnTriangulation, thePolygon2: Poly_PolygonOnTriangulation, theTriangulation: Poly_Triangulation, theLocation: TopLoc_Location) -> None: ...
	@staticmethod
	def UseLocation(thePnt: gp_Pnt, theLoc: TopLoc_Location) -> gp_Pnt: ...

class BRepMesh_ShapeVisitor(IMeshTools_ShapeVisitor):
	def __init__(self, theModel: IMeshData_Model) -> None: ...
	@overload
	def Visit(self, theFace: TopoDS_Face) -> None: ...
	@overload
	def Visit(self, theEdge: TopoDS_Edge) -> None: ...

class BRepMesh_Triangle:
	@overload
	def __init__(self) -> None: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def IsEqual(self, theOther: BRepMesh_Triangle) -> bool: ...
	def Movability(self) -> BRepMesh_DegreeOfFreedom: ...
	def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...

class BRepMesh_Vertex:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theUV: gp_XY, theLocation3d: int, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...
	@overload
	def __init__(self, theU: float, theV: float, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...
	def ChangeCoord(self) -> gp_XY: ...
	def Coord(self) -> gp_XY: ...
	def HashCode(self, theUpperBound: int) -> int: ...
	def Initialize(self, theUV: gp_XY, theLocation3d: int, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...
	def IsEqual(self, theOther: BRepMesh_Vertex) -> bool: ...
	def Location3d(self) -> int: ...
	def Movability(self) -> BRepMesh_DegreeOfFreedom: ...
	def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...

class BRepMesh_VertexInspector(NCollection_CellFilter_InspectorXY):
	@overload
	def __init__(self, theAllocator: NCollection_IncAllocator) -> None: ...
	def Add(self, theVertex: BRepMesh_Vertex) -> int: ...
	def Clear(self) -> None: ...
	def Delete(self, theIndex: int) -> None: ...
	def GetCoincidentPoint(self) -> int: ...
	def GetListOfDelPoints(self) -> False: ...
	def GetVertex(self, theIndex: int) -> BRepMesh_Vertex: ...
	def Inspect(self, theTargetIndex: int) -> NCollection_CellFilter_Action: ...
	@staticmethod
	def IsEqual(theIndex: int, theTargetIndex: int) -> bool: ...
	def NbVertices(self) -> int: ...
	def SetPoint(self, thePoint: gp_XY) -> None: ...
	@overload
	def SetTolerance(self, theTolerance: float) -> None: ...
	@overload
	def SetTolerance(self, theToleranceX: float, theToleranceY: float) -> None: ...

class BRepMesh_VertexTool(Standard_Transient):
	@overload
	def __init__(self, theAllocator: NCollection_IncAllocator) -> None: ...
	def Add(self, theVertex: BRepMesh_Vertex, isForceAdd: bool) -> int: ...
	def DeleteVertex(self, theIndex: int) -> None: ...
	def Extent(self) -> int: ...
	def FindIndex(self, theVertex: BRepMesh_Vertex) -> int: ...
	def FindKey(self, theIndex: int) -> BRepMesh_Vertex: ...
	def GetListOfDelNodes(self) -> False: ...
	def GetTolerance(self) -> Tuple[float, float]: ...
	def IsEmpty(self) -> bool: ...
	def RemoveLast(self) -> None: ...
	@overload
	def SetCellSize(self, theSize: float) -> None: ...
	@overload
	def SetCellSize(self, theSizeX: float, theSizeY: float) -> None: ...
	@overload
	def SetTolerance(self, theTolerance: float) -> None: ...
	@overload
	def SetTolerance(self, theToleranceX: float, theToleranceY: float) -> None: ...
	def Substitute(self, theIndex: int, theVertex: BRepMesh_Vertex) -> None: ...

class BRepMesh_DelabellaBaseMeshAlgo(BRepMesh_CustomBaseMeshAlgo):
	def __init__(self) -> None: ...

class BRepMesh_Edge(BRepMesh_OrientedEdge):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theFirstNode: int, theLastNode: int, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...
	def IsEqual(self, theOther: BRepMesh_Edge) -> bool: ...
	def IsSameOrientation(self, theOther: BRepMesh_Edge) -> bool: ...
	def Movability(self) -> BRepMesh_DegreeOfFreedom: ...
	def SetMovability(self, theMovability: BRepMesh_DegreeOfFreedom) -> None: ...

class BRepMesh_IncrementalMesh(BRepMesh_DiscretRoot):
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, theShape: TopoDS_Shape, theLinDeflection: float, isRelative: Optional[bool] = False, theAngDeflection: Optional[float] = 0.5, isInParallel: Optional[bool] = False) -> None: ...
	@overload
	def __init__(self, theShape: TopoDS_Shape, theParameters: IMeshTools_Parameters, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	def ChangeParameters(self) -> IMeshTools_Parameters: ...
	@staticmethod
	def Discret(theShape: TopoDS_Shape, theLinDeflection: float, theAngDeflection: float, theAlgo: BRepMesh_DiscretRoot) -> int: ...
	def GetStatusFlags(self) -> int: ...
	def IsModified(self) -> bool: ...
	@staticmethod
	def IsParallelDefault() -> bool: ...
	def Parameters(self) -> IMeshTools_Parameters: ...
	@overload
	def Perform(self, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	@overload
	def Perform(self, theContext: IMeshTools_Context, theRange: Optional[Message_ProgressRange] = Message_ProgressRange()) -> None: ...
	@staticmethod
	def SetParallelDefault(isInParallel: bool) -> None: ...

class BRepMesh_DelaunayBaseMeshAlgo(BRepMesh_ConstrainedBaseMeshAlgo):
	def __init__(self) -> None: ...

#classnotwrapped
class BRepMesh_WireInterferenceChecker: ...

#classnotwrapped
class BRepMesh_EdgeTessellator: ...

#classnotwrapped
class BRepMesh_EdgeTessellationExtractor: ...

#classnotwrapped
class BRepMesh_EdgeParameterProvider: ...

#classnotwrapped
class BRepMesh_FastDiscret: ...

#classnotwrapped
class BRepMesh_CustomDelaunayBaseMeshAlgo: ...

#classnotwrapped
class BRepMesh_NodeInsertionMeshAlgo: ...

#classnotwrapped
class BRepMesh_ConstrainedBaseMeshAlgo: ...

#classnotwrapped
class BRepMesh_CustomBaseMeshAlgo: ...

#classnotwrapped
class BRepMesh_DelaunayDeflectionControlMeshAlgo: ...

#classnotwrapped
class BRepMesh_DelaunayNodeInsertionMeshAlgo: ...

# harray1 classes
# harray2 classes
# hsequence classes

BRepMesh_CircleInspector_IsEqual = BRepMesh_CircleInspector.IsEqual
BRepMesh_CircleTool_MakeCircle = BRepMesh_CircleTool.MakeCircle
BRepMesh_Deflection_ComputeAbsoluteDeflection = BRepMesh_Deflection.ComputeAbsoluteDeflection
BRepMesh_Deflection_ComputeDeflection = BRepMesh_Deflection.ComputeDeflection
BRepMesh_Deflection_ComputeDeflection = BRepMesh_Deflection.ComputeDeflection
BRepMesh_Deflection_ComputeDeflection = BRepMesh_Deflection.ComputeDeflection
BRepMesh_Deflection_IsConsistent = BRepMesh_Deflection.IsConsistent
BRepMesh_DiscretFactory_Get = BRepMesh_DiscretFactory.Get
BRepMesh_EdgeDiscret_CreateEdgeTessellationExtractor = BRepMesh_EdgeDiscret.CreateEdgeTessellationExtractor
BRepMesh_EdgeDiscret_CreateEdgeTessellator = BRepMesh_EdgeDiscret.CreateEdgeTessellator
BRepMesh_EdgeDiscret_CreateEdgeTessellator = BRepMesh_EdgeDiscret.CreateEdgeTessellator
BRepMesh_EdgeDiscret_Tessellate2d = BRepMesh_EdgeDiscret.Tessellate2d
BRepMesh_EdgeDiscret_Tessellate3d = BRepMesh_EdgeDiscret.Tessellate3d
BRepMesh_GeomTool_CellsCount = BRepMesh_GeomTool.CellsCount
BRepMesh_GeomTool_SquareDeflectionOfSegment = BRepMesh_GeomTool.SquareDeflectionOfSegment
BRepMesh_ShapeTool_AddInFace = BRepMesh_ShapeTool.AddInFace
BRepMesh_ShapeTool_BoxMaxDimension = BRepMesh_ShapeTool.BoxMaxDimension
BRepMesh_ShapeTool_CheckAndUpdateFlags = BRepMesh_ShapeTool.CheckAndUpdateFlags
BRepMesh_ShapeTool_MaxFaceTolerance = BRepMesh_ShapeTool.MaxFaceTolerance
BRepMesh_ShapeTool_NullifyEdge = BRepMesh_ShapeTool.NullifyEdge
BRepMesh_ShapeTool_NullifyEdge = BRepMesh_ShapeTool.NullifyEdge
BRepMesh_ShapeTool_NullifyFace = BRepMesh_ShapeTool.NullifyFace
BRepMesh_ShapeTool_Range = BRepMesh_ShapeTool.Range
BRepMesh_ShapeTool_Range = BRepMesh_ShapeTool.Range
BRepMesh_ShapeTool_UVPoints = BRepMesh_ShapeTool.UVPoints
BRepMesh_ShapeTool_UpdateEdge = BRepMesh_ShapeTool.UpdateEdge
BRepMesh_ShapeTool_UpdateEdge = BRepMesh_ShapeTool.UpdateEdge
BRepMesh_ShapeTool_UpdateEdge = BRepMesh_ShapeTool.UpdateEdge
BRepMesh_ShapeTool_UseLocation = BRepMesh_ShapeTool.UseLocation
BRepMesh_VertexInspector_IsEqual = BRepMesh_VertexInspector.IsEqual
BRepMesh_IncrementalMesh_Discret = BRepMesh_IncrementalMesh.Discret
BRepMesh_IncrementalMesh_IsParallelDefault = BRepMesh_IncrementalMesh.IsParallelDefault
BRepMesh_IncrementalMesh_SetParallelDefault = BRepMesh_IncrementalMesh.SetParallelDefault
