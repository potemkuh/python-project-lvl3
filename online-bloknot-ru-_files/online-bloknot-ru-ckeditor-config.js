/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */
//CKEDITOR.env.isCompatible = true;
CKEDITOR.editorConfig = function( config ) {
    
    config.removePlugins = 'menu,contextmenu';
	// Define changes to default configuration here.
	// For complete reference see:
	// http://docs.ckeditor.com/#!/api/CKEDITOR.config
    
	// The toolbar groups arrangement, optimized for a single toolbar row.
	config.toolbarGroups = [
		{ name: 'document',	   groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'clipboard',   groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing',     groups: [ 'find', 'selection', 'spellchecker' ] },
		{ name: 'forms' },
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph',   groups: [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
		{ name: 'links' },
		{ name: 'insert' },
		{ name: 'styles' },
		{ name: 'colors' },
		{ name: 'tools' },
		{ name: 'others' },
		{ name: 'about' }
	];

	// The default plugins included in the basic setup define some buttons that
	// are not needed in a basic editor. They are removed here.
	config.removeButtons = 'Cut,Copy,Paste,Undo,Redo,Anchor,Subscript,Superscript,Indent,Outdent,Unlink';
    config.autoGrow_onStartup = true;
    config.autoGrow_minHeight = 670;
    
	// Dialog windows are also simplified.
	config.removeDialogTabs = 'link:advanced;link:target';
	
	// Extra plugins
	config.extraPlugins = 'onchange,print,confighelper,save,link,autogrow,pastetext'; //devtools tabletools
    config.forcePasteAsPlainText = true;
	
	// Calculate custom height
	//config.height = window.innerHeight - 275 + 19;
    // Auto sizing
    //config.width = "auto";
    //config.height = getNoteHeight();

	// Custom toolbar
	config.toolbar_Note =
	[
		{ name: 'global', 	items: ['Bold','Italic','Underline','Strike','BGColor','TextColor','BulletedList','NumberedList','Link','Print','Save'] }
	];
    
	config.toolbar = 'Note';
	
	// Modified dialogues
	config.hideDialogFields = 'link:info:linkType;table:info:txtCellSpace;table:info:txtCellPad;table:info:txtBorder';
	config.removeDialogFields = 'link:info:protocol;table:info:selHeaders;table:info:cmbAlign;table:info:txtCaption;table:info:txtSummary';
	config.dialogFieldsDefaultValues = {
		table: {
			info: {
				txtCellSpace: '1',
				txtCellPad: '1',
				txtBorder: '1'
			}
		},
		link: {
			info: {
				linkType: 'url',
				protocol: 'http://'
			},
			target: {
				linktargetType: '_blank'
			}
		}
	}
    
    // Styles custom

};
