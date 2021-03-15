import vstruct
from vstruct.primitives import *


class Dwarf32CompileHeader(vstruct.VStruct):
    def __init__(self, bigend=False):
        vstruct.VStruct.__init__(self)
        self.length = v_uint32(bigend=bigend)
        self.version = v_uint16(bigend=bigend)
        self.abbrev_offset = v_uint32(bigend=bigend)
        self.ptrsize= v_uint8()


class Dwarf32TypeHeader(vstruct.VStruct):
    def __init__(self, bigend=False):
        vstruct.VStruct.__init__(self)
        self.length = v_uint32(bigend=bigend)
        self.version = v_uint16(bigend=bigend)
        self.abbrev_offset = v_uint32(bigend=bigend)
        self.ptrsize= v_uint8()
        self.type_sig = v_uint64(bigend=bigend)
        self.type_offset = v_uint32(bigend=bigend)


class Dwarf64CompileHeader(vstruct.VStruct):
    def __init__(self, bigend=False):
        vstruct.VStruct.__init__(self)
        self.length = v_uint96(bigend=bigend)
        self.version = v_uint16(bigend=bigend)
        self.abbrev_offset = v_uint64(bigend=bigend)
        self.ptrsize= v_uint8()


class Dwarf64TypeHeader(vstruct.VStruct):
    def __init__(self, bigend=False):
        vstruct.VStruct.__init__(self)
        self.length = v_uint96(bigend=bigend)
        self.version = v_uint16(bigend=bigend)
        self.abbrev_offset = v_uint64(bigend=bigend)
        self.ptrsize = v_uint8()
        self.type_sig = v_uint64(bigend=bigend)
        self.type_offset = v_uint64(bigend=bigend)

# DWARF Debugging info Enums

DW_CHILDREN_no = 0x0
DW_CHILDREN_yes = 0x1

# DWARF Tag Encodings
DW_TAG_array_type = 0x1
DW_TAG_class_type = 0x2
DW_TAG_entry_point = 0x3
DW_TAG_enumeration_type = 0x4
DW_TAG_formal_parameter = 0x5
DW_TAG_imported_declaration = 0x8
DW_TAG_label = 0xa
DW_TAG_lexical_block = 0xb
DW_TAG_member = 0xd
DW_TAG_pointer_type = 0xf
DW_TAG_reference_type = 0x10
DW_TAG_compile_unit = 0x11
DW_TAG_string_type = 0x12
DW_TAG_structure_type = 0x13
DW_TAG_subroutine_type = 0x15
DW_TAG_typedef = 0x16
DW_TAG_union_type = 0x17
DW_TAG_unspecified_parameters = 0x18
DW_TAG_variant = 0x19
DW_TAG_common_block = 0x1a
DW_TAG_common_inclusion = 0x1b
DW_TAG_inheritance = 0x1c
DW_TAG_inlined_subroutine = 0x1d
DW_TAG_module = 0x1e
DW_TAG_ptr_to_member_type = 0x1f
DW_TAG_set_type = 0x20
DW_TAG_subrange_type = 0x21
DW_TAG_with_stmt = 0x22
DW_TAG_access_declaration = 0x23
DW_TAG_base_type = 0x24
DW_TAG_catch_block = 0x25
DW_TAG_const_type = 0x26
DW_TAG_constant = 0x27
DW_TAG_enumerator = 0x28
DW_TAG_file_type = 0x29
DW_TAG_friend = 0x2a
DW_TAG_namelist = 0x2b
DW_TAG_namelist_item = 0x2c
DW_TAG_packed_type = 0x2d
DW_TAG_subprogram = 0x2e
DW_TAG_template_type_parameter = 0x2f
DW_TAG_template_value_parameter = 0x30
DW_TAG_thrown_type = 0x31
DW_TAG_try_block = 0x32
DW_TAG_variant_part = 0x33
DW_TAG_variable = 0x34
DW_TAG_volatile_type = 0x35
DW_TAG_dwarf_procedure = 0x36
DW_TAG_restrict_type = 0x37
DW_TAG_interface_type = 0x38
DW_TAG_namespace = 0x39
DW_TAG_imported_module = 0x3a
DW_TAG_unspecified_type = 0x3b
DW_TAG_partial_unit = 0x3c
DW_TAG_imported_unit = 0x3d
DW_TAG_condition = 0x3f
DW_TAG_shared_type = 0x40
DW_TAG_type_unit = 0x41  # V4
DW_TAG_rvalue_reference_type = 0x42  # V4
DW_TAG_template_alias = 0x43  # V4
DW_TAG_lo_user = 0x4080
DW_TAG_hi_user = 0xffff


# DWARF Attribute Encodings
DW_AT_sibling = 0x1
DW_AT_location = 0x2
DW_AT_name = 0x3
DW_AT_ordering = 0x9
DW_AT_byte_size = 0xb
DW_AT_bit_offset = 0xc
DW_AT_bit_size = 0xd
DW_AT_stmt_list = 0x10
DW_AT_low_pc = 0x11
DW_AT_high_pc = 0x12
DW_AT_language = 0x13
DW_AT_discr = 0x15
DW_AT_discr_value = 0x16
DW_AT_visibility = 0x17
DW_AT_import = 0x18
DW_AT_string_length = 0x19
DW_AT_common_reference = 0x1a
DW_AT_comp_dir = 0x1b
DW_AT_const_value = 0x1c
DW_AT_containing_type = 0x1d
DW_AT_default_value = 0x1e
DW_AT_inline = 0x20
DW_AT_is_optional = 0x21
DW_AT_lower_bound = 0x22
DW_AT_producer = 0x25
DW_AT_prototyped = 0x27
DW_AT_return_addr = 0x2a
DW_AT_start_scope = 0x2c
DW_AT_bit_stride = 0x2e
DW_AT_upper_bound = 0x2f
DW_AT_abstract_origin = 0x31
DW_AT_accessibility = 0x32
DW_AT_address_class = 0x33
DW_AT_artificial = 0x34
DW_AT_base_types = 0x35
DW_AT_calling_convention = 0x36
DW_AT_count = 0x37
DW_AT_data_member_location = 0x38
DW_AT_decl_column = 0x39
DW_AT_decl_file = 0x3a
DW_AT_decl_line = 0x3b
DW_AT_declaration = 0x3c
DW_AT_discr_list = 0x3d
DW_AT_encoding = 0x3e
DW_AT_external = 0x3f
DW_AT_frame_base = 0x40
DW_AT_friend = 0x41
DW_AT_identifier_case = 0x42
DW_AT_macro_info = 0x43
DW_AT_namelist_item = 0x44
DW_AT_priority = 0x45
DW_AT_segment = 0x46
DW_AT_specification = 0x47
DW_AT_static_link = 0x48
DW_AT_type = 0x49
DW_AT_use_location = 0x4a
DW_AT_variable_paramter = 0x4b
DW_AT_virtuality = 0x4c
DW_AT_vtable_elem_location = 0x4d
DW_AT_allocated = 0x4e
DW_AT_associated = 0x4f
DW_AT_data_location = 0x50
DW_AT_byte_stride = 0x51
DW_AT_entry_pc = 0x52
DW_AT_use_UTF8 = 0x53
DW_AT_extension = 0x54
DW_AT_ranges = 0x55
DW_AT_trampoline = 0x56
DW_AT_call_column = 0x57
DW_AT_call_file = 0x58
DW_AT_call_line = 0x59
DW_AT_description = 0x5a
DW_AT_binary_scale = 0x5b
DW_AT_decimal_scale = 0x5c
DW_AT_small = 0x5d
DW_AT_decimal_sign = 0x5e
DW_AT_digit_count = 0x5f
DW_AT_picture_string = 0x60
DW_AT_mutable = 0x61
DW_AT_threads_scaled = 0x62
DW_AT_explicit = 0x63
DW_AT_object_pointer = 0x64
DW_AT_endianity = 0x65
DW_AT_elemental = 0x66
DW_AT_pure = 0x67
DW_AT_recursive = 0x68
DW_AT_signature = 0x69  # V4
DW_AT_main_subprogram = 0x6a  # V4
DW_AT_data_bit_offset = 0x6b  # V4
DW_AT_const_expr = 0x6c  # V4
DW_AT_enum_class = 0xd  # V4
DW_AT_linkage_name = 0x6e  # V4
# v5 only. can appear in v4 as gnu extensions
DW_AT_string_length_bit_size = 0x6f
DW_AT_string_length_byte_size = 0x70
DW_AT_rank = 0x71
DW_AT_str_offsets_base = 0x72
DW_AT_addr_base = 0x73
DW_AT_rnglists_base = 0x74
# reserved
DW_AT_dwo_name = 0x76
DW_AT_reference = 0x77
DW_AT_rvalue_reference = 0x78
DW_AT_macros = 0x79
DW_AT_call_all_calls = 0x7a
DW_AT_call_all_source_calls = 0x7b
DW_AT_call_all_tail_calls = 0x7c
DW_AT_call_return_pc = 0x7d
DW_AT_call_value = 0x7e
DW_AT_call_origin = 0x7f
DW_AT_call_parameter = 0x80
DW_AT_call_pc = 0x81
DW_AT_call_tail_call = 0x82
DW_AT_call_target = 0x83
DW_AT_call_target_clobbered = 0x84
DW_AT_call_data_location = 0x85
DW_AT_call_data_value = 0x86
DW_AT_no_return = 0x87
DW_AT_alignment = 0x88
DW_AT_export_symbols = 0x89
DW_AT_deleted = 0x8a
DW_AT_defaulted = 0x8b
DW_AT_loclists_base = 0x8c
DW_AT_lo_user = 0x2000
DW_AT_hi_user = 0x3fff


# GNU Attributes. Typically only for v4 now since a lot got mainlined in v5
DW_AT_GNU_vector = 0x2107
DW_AT_GNU_guarded_by = 0x2108
DW_AT_GNU_pt_guarded_by = 0x2109
DW_AT_GNU_guarded = 0x210a
DW_AT_GNU_pt_guarded = 0x210b
DW_AT_GNU_locks_excluded = 0x210c
DW_AT_GNU_exclusive_locks_required = 0x210d
DW_AT_GNU_shared_locks_required = 0x210e
DW_AT_GNU_odr_signature = 0x210f
DW_AT_GNU_template_name = 0x2110
DW_AT_GNU_call_site_value = 0x2111
DW_AT_GNU_call_site_data_value = 0x2112
DW_AT_GNU_call_site_target = 0x2113
DW_AT_GNU_call_site_target_clobbered = 0x2114
DW_AT_GNU_tail_call = 0x2115
DW_AT_GNU_all_tail_call_sites = 0x2116
DW_AT_GNU_all_call_sites = 0x2117
DW_AT_GNU_all_source_call_sites = 0x2118
DW_AT_GNU_macros = 0x2119
DW_AT_GNU_deleted = 0x211a
DW_AT_GNU_dwo_name = 0x2130
DW_AT_GNU_dwo_id = 0x2131
DW_AT_GNU_ranges_base = 0x2132
DW_AT_GNU_addr_base = 0x2133
DW_AT_GNU_pubnames = 0x2134
DW_AT_GNU_pubtypes = 0x2135

dwarf_attribute_names = {
    DW_AT_sibling: 'sibling',
    DW_AT_location: 'location',
    DW_AT_name: 'name',
    DW_AT_ordering: 'ordering',
    DW_AT_byte_size: 'byte_size',
    DW_AT_bit_offset: 'bit_offset',
    DW_AT_bit_size: 'bit_size',
    DW_AT_stmt_list: 'stmt_list',
    DW_AT_low_pc: 'low_pc',
    DW_AT_high_pc: 'high_pc',
    DW_AT_language: 'language',
    DW_AT_discr: 'discr',
    DW_AT_discr_value: 'discr_value',
    DW_AT_visibility: 'visibility',
    DW_AT_import: 'import',
    DW_AT_string_length: 'string_length',
    DW_AT_common_reference: 'common_reference',
    DW_AT_comp_dir: 'comp_dir',
    DW_AT_const_value: 'const_value',
    DW_AT_containing_type: 'containing_type',
    DW_AT_default_value: 'default_value',
    DW_AT_inline: 'inline',
    DW_AT_is_optional: 'is_optional',
    DW_AT_lower_bound: 'lower_bound',
    DW_AT_producer: 'producer',
    DW_AT_prototyped: 'prototyped',
    DW_AT_return_addr: 'return_addr',
    DW_AT_start_scope: 'start_scope',
    DW_AT_bit_stride: 'bit_stride',
    DW_AT_upper_bound: 'uppder_bound',
    DW_AT_abstract_origin: 'abstract_origin',
    DW_AT_accessibility: 'accessibility',
    DW_AT_address_class: 'address_class',
    DW_AT_artificial: 'artificial',
    DW_AT_base_types: 'base_types',
    DW_AT_calling_convention: 'calling_convention',
    DW_AT_count: 'count',
    DW_AT_data_member_location: 'data_member_location',
    DW_AT_decl_column: 'decl_column',
    DW_AT_decl_file: 'decl_file',
    DW_AT_decl_line: 'decl_line',
    DW_AT_declaration: 'declaration',
    DW_AT_discr_list: 'discr_list',
    DW_AT_encoding: 'encoding',
    DW_AT_external: 'external',
    DW_AT_frame_base: 'frame_base',
    DW_AT_friend: 'friend',
    DW_AT_identifier_case: 'identifier_case',
    DW_AT_macro_info: 'macro_info',
    DW_AT_namelist_item: 'namelist_item',
    DW_AT_priority: 'prority',
    DW_AT_segment: 'segment',
    DW_AT_specification: 'specification',
    DW_AT_static_link: 'static_link',
    DW_AT_type: 'type',
    DW_AT_use_location: 'use_location',
    DW_AT_variable_paramter: 'variable_parameter',
    DW_AT_virtuality: 'virtuality',
    DW_AT_vtable_elem_location: 'vtable_elem_location',
    DW_AT_allocated: 'allocated',
    DW_AT_associated: 'associated',
    DW_AT_data_location: 'data_location',
    DW_AT_byte_stride: 'byte_stride',
    DW_AT_entry_pc: 'entry_pc',
    DW_AT_use_UTF8: 'use_utf8',
    DW_AT_extension: 'extension',
    DW_AT_ranges: 'ranges',
    DW_AT_trampoline: 'trampoline',
    DW_AT_call_column: 'call_column',
    DW_AT_call_file: 'call_file',
    DW_AT_call_line: 'call_line',
    DW_AT_description: 'description',
    DW_AT_binary_scale: 'binary_scale',
    DW_AT_decimal_scale: 'decimal_scale',
    DW_AT_small: 'small',
    DW_AT_decimal_sign: 'decimal_sign',
    DW_AT_digit_count: 'digit_count',
    DW_AT_picture_string: 'picture_string',
    DW_AT_mutable: 'mutable',
    DW_AT_threads_scaled: 'threads_scaled',
    DW_AT_explicit: 'explicit',
    DW_AT_object_pointer: 'object_pointer',
    DW_AT_endianity: 'endianity',
    DW_AT_elemental: 'elemental',
    DW_AT_pure: 'pure',
    DW_AT_recursive: 'recursive',
    DW_AT_signature: 'signature',
    DW_AT_main_subprogram: 'main_subprogram',
    DW_AT_data_bit_offset: 'data_bit_offset',
    DW_AT_const_expr: 'const_expr',
    DW_AT_enum_class: 'enum_class',
    DW_AT_linkage_name: 'linkage_name',

    DW_AT_string_length_bit_size: 'string_length_bit_size',
    DW_AT_string_length_byte_size: 'string_length_byte_size',
    DW_AT_rank: 'rank',
    DW_AT_str_offsets_base: 'str_offsets_base',
    DW_AT_addr_base: 'addr_base',
    DW_AT_rnglists_base: 'rnglists_base',
    DW_AT_dwo_name: 'dwo_name',
    DW_AT_reference: 'reference',
    DW_AT_rvalue_reference: 'rvalue_reference',
    DW_AT_macros: 'macros',
    DW_AT_call_all_calls: 'call_all_calls',
    DW_AT_call_all_source_calls: 'call_all_source_calls',
    DW_AT_call_all_tail_calls: 'call_all_tail_calls',
    DW_AT_call_return_pc: 'call_return_pc',
    DW_AT_call_value: 'call_value',
    DW_AT_call_origin: 'call_origin',
    DW_AT_call_parameter: 'call_parameter',
    DW_AT_call_pc: 'call_pc',
    DW_AT_call_tail_call: 'call_tail_call',
    DW_AT_call_target: 'call_target',
    DW_AT_call_target_clobbered: 'call_target_clobbered',
    DW_AT_call_data_location: 'call_data_location',
    DW_AT_call_data_value: 'call_data_value',
    DW_AT_no_return: 'no_return',
    DW_AT_alignment: 'alignment',
    DW_AT_export_symbols: 'export_symbols',
    DW_AT_deleted: 'deleted',
    DW_AT_defaulted: 'defaulted',
    DW_AT_loclists_base: 'loclists_base',
    DW_AT_lo_user: 'lo_user',
    DW_AT_hi_user: 'hi_user',
}

gnu_attribute_names = {
    DW_AT_GNU_vector: 'vector',
    DW_AT_GNU_guarded_by: 'guarded_by',
    DW_AT_GNU_pt_guarded_by: 'pt_guarded_by',
    DW_AT_GNU_guarded: 'guarded',
    DW_AT_GNU_pt_guarded: 'pt_guarded',
    DW_AT_GNU_locks_excluded: 'locks_excluded',
    DW_AT_GNU_exclusive_locks_required: 'exclusive_locks_required',
    DW_AT_GNU_shared_locks_required: 'shared_locks_required',
    DW_AT_GNU_odr_signature: 'odr_signature',
    DW_AT_GNU_template_name: 'template_name',
    DW_AT_GNU_call_site_value: 'call_site_value',
    DW_AT_GNU_call_site_data_value: 'call_site_data_value',
    DW_AT_GNU_call_site_target: 'call_site_target',
    DW_AT_GNU_call_site_target_clobbered: 'call_site_target_clobbered',
    DW_AT_GNU_tail_call: 'tail_call',
    DW_AT_GNU_all_tail_call_sites: 'all_tail_call_sites',
    DW_AT_GNU_all_call_sites: 'all_call_sites',
    DW_AT_GNU_all_source_call_sites: 'all_source_call_sites',
    DW_AT_GNU_macros: 'macros',
    DW_AT_GNU_deleted: 'deleted',
    DW_AT_GNU_dwo_name: 'dwo_name',
    DW_AT_GNU_dwo_id: 'dwo_id',
    DW_AT_GNU_ranges_base: 'ranges_base',
    DW_AT_GNU_addr_base: 'addr_base',
    DW_AT_GNU_pubnames: 'pubnames',
    DW_AT_GNU_pubtypes: 'pubtypes',
}

# DWARF Attribute Form Encodings
DW_FORM_addr = 0x1
DW_FORM_block2 = 0x3
DW_FORM_block4 = 0x4
DW_FORM_data2 = 0x5
DW_FORM_data4 = 0x6
DW_FORM_data8 = 0x7
DW_FORM_string = 0x8
DW_FORM_block = 0x9
DW_FORM_block1 = 0xa
DW_FORM_data1 = 0xb
DW_FORM_flag = 0xc
DW_FORM_sdata = 0xd
DW_FORM_strp = 0xe
DW_FORM_udata = 0xf
DW_FORM_ref_addr = 0x10
DW_FORM_ref1 = 0x11
DW_FORM_ref2 = 0x12
DW_FORM_ref4 = 0x13
DW_FORM_ref8 = 0x14
DW_FORM_ref_udata = 0x15
DW_FORM_indirect = 0x16
DW_FORM_sec_offset = 0x17  # V4
DW_FORM_exprloc = 0x18  # V4
DW_FORM_flag_present = 0x19  # V4

DW_FORM_strx = 0x1a
DW_FORM_addrx = 0x1b
DW_FORM_ref_sup4 = 0x1c
DW_FORM_strp_sup = 0x1d
DW_FORM_data16 = 0x1e
DW_FORM_line_strp = 0x1f

DW_FORM_ref_sig8 = 0x20  # V4

DW_FORM_implicit_const = 0x21
DW_FORM_loclistx = 0x22
DW_FORM_rnglistx = 0x23
DW_FORM_ref_sup8 = 0x24
DW_FORM_strx1 = 0x25
DW_FORM_strx2 = 0x26
DW_FORM_strx3 = 0x27
DW_FORM_strx4 = 0x28
DW_FORM_addrx1 = 0x29
DW_FORM_addrx2 = 0x2a
DW_FORM_addrx3 = 0x2b
DW_FORM_addrx4 = 0x2c


DW_LANG_C89 = 0x01
DW_LANG_C = 0x02
DW_LANG_Ada83 = 0x03
DW_LANG_Cpp = 0x04
DW_LANG_Cobol74 = 0x05
DW_LANG_Cobol85 = 0x06
DW_LANG_Fortran77 = 0x07
DW_LANG_Fortran90 = 0x08
DW_LANG_Pascal83 = 0x09
DW_LANG_Modula2 = 0x0a
DW_LANG_Java = 0x0b
DW_LANG_C99 = 0x0c
DW_LANG_Ada95 = 0x0d
DW_LANG_Fortran95 = 0x0e
DW_LANG_PLI = 0x0f
DW_LANG_ObjC = 0x10
DW_LANG_ObjCpp = 0x11
DW_LANG_UPC = 0x12
DW_LANG_D = 0x13
DW_LANG_Python = 0x14
DW_LANG_lo_user = 0x8000
DW_LANG_hi_user = 0xffff

DW_ID_case_sensitive = 0x00
DW_ID_up_case = 0x01
DW_ID_down_case = 0x02
DW_ID_case_insensitive = 0x03
