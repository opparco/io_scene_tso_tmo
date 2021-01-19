
"""tso export operator
"""

import bpy
from bpy_extras.io_utils import ExportHelper
from io_scene_tso_tmo import tso_export

class TsoExportOperator(bpy.types.Operator, ExportHelper):
	bl_idname = "export_scene.tso"
	bl_label = "Export TSO"
	bl_options = {'PRESET'}

	filename_ext = ".tso"
	filter_glob: bpy.props.StringProperty(default="*.tso", options={'HIDDEN'})

	def execute(self, context):
		import os

		dest_file = self.properties.filepath
		ref_file = os.path.dirname(__file__) + "/resources/mod1.tso"
		tso_export.export_tsofile(dest_file, ref_file)
		return {'FINISHED'}

