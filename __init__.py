bl_info = {
	"name": "TechArts3D tso format and tmo format",
	"author": "opparco",
	"version": (1, 0, 0),
	"blender": (2, 80, 0),
	"category": "Import-Export",
}

import bpy
from io_scene_tso_tmo import tso_import_op, tmo_import_op, tso_export_op


def menu_func_import(self, context):
	self.layout.operator(tso_import_op.TsoImportOperator.bl_idname, text="TechArts3D tso (.tso)")
	self.layout.operator(tmo_import_op.TmoImportOperator.bl_idname, text="TechArts3D tmo (.tmo)")

def menu_func_export(self, context):
	self.layout.operator(tso_export_op.TsoExportOperator.bl_idname, text="TechArts3D tso (.tso)")


classes = (
	tso_import_op.TsoImportOperator,
	tmo_import_op.TmoImportOperator,
	tso_export_op.TsoExportOperator,
)

def register():
	for cls in classes:
		bpy.utils.register_class(cls)

	bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
	bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
	bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)
	bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

	for cls in classes:
		bpy.utils.unregister_class(cls)


if __name__ == "__main__":
	register()

