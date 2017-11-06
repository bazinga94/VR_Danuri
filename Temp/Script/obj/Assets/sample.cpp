#include "ESharp.h"
#include "ESDllInterface.h"
#include "Engine.h"
#include "sample.h"
#include "Math3D.Range.h"
#include "Math3D.BoundingBox2D.h"
#include "Math3D.Color.h"
#include "Math3D.Polygon.h"
#include "Math3D.Vector4.h"
#include "Math3D.Line.h"
#include "Math3D.Plane.h"
#include "Math3D.Frustum.h"
#include "Math3D.Collision.h"
#include "Math3D.Vector2.h"
#include "Math3D.Util.h"
#include "Math3D.BoundingBox.h"
#include "Math3D.Point.h"
#include "Math3D.Matrix4x4.h"
#include "Math3D.Quaternion.h"
#include "Math3D.Rect.h"
#include "Math3D.Matrix3.h"
#include "Math3D.Vector3.h"


int sample::OnMessage(wstring msg, int arg0, Vector4* arg1, Vector4* arg2)
{
    return 0;
}


int sample::Update()
{
    Log(L"hello danuri", 0, 0.0f);
    return 0;
}


sample::sample()
{
}


const vector<string> sample::mFieldNames = {};
const vector<string> sample::mFieldTypes = {};
const vector<string> sample::mFieldAccessors = {};


const char* sample::__GetClassName__()
{
    return "sample";
}


unsigned int sample::__GetFieldNum__()
{
    return 0;
}


const char* sample::__GetFieldName__(unsigned int i)
{
    if (i >= mFieldNames.size())	return nullptr;
    else							return mFieldNames[i].c_str();
}


const char* sample::__GetFieldType__(unsigned int i)
{
    if (i >= mFieldTypes.size())	return nullptr;
    else							return mFieldTypes[i].c_str();
}


const char* sample::__GetFieldAccessor__(unsigned int i)
{
    if (i >= mFieldAccessors.size())	return nullptr;
    else								return mFieldAccessors[i].c_str();
}


int sample::__ReadField__(string fieldName, void* ptr, int* len)
{
    string arrayFieldName = "";
    int arrayIndex = 0;
    SeparateArrayFieldName(fieldName, arrayFieldName, arrayIndex);

    return 0;
}


int sample::__WriteField__(string fieldName, void* ptr, int len, int typeInfo)
{
    void* buf = nullptr;

    string arrayFieldName = "";
    int arrayIndex = 0;
    SeparateArrayFieldName(fieldName, arrayFieldName, arrayIndex);

    if (buf == nullptr)
    {
        return 1;
    }

    memcpy(buf, ptr, len);
    return 0;
}
