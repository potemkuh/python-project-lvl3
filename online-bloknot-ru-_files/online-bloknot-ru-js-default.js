var timer;
var $WYSIWYG;


function pad2(number) {
   return (number < 10 ? '0' : '') + number
}

function save() {
	var obj=$('#note').val();
	if (typeof obj != "undefined") 
		$.jStorage.set("online-bloknot", obj);
}

function saveTextAsFile(){
	var date = new Date();
	var dateFormat = 	pad2(date.getDate()) + '.' + 
						pad2(date.getMonth()+1) + '.' + 
						date.getFullYear() + ', ' + 
						pad2(date.getHours()) + '.' + 
						pad2(date.getMinutes());
    var fileNameToSaveAs = "Онлайн-блокнот — " + dateFormat;
    
    var $obj = $("<div/>");
    $obj.html( 
        '<div style="font-family:Calibri,sans-serif;font-size:11pt;">' +
            $("#note").val()
                .replace(/background-color:\s*([^;"]+)/g, 'background:$1;mso-highlight:$1') +
        '</div>'
    );

    $obj.wordExport(fileNameToSaveAs);
}

function getNoteHeight(){
    return $('#content').height() - 40;
}

$(document).ready(function(){
	var NOTE = $('#note');

    if (NOTE.length > 0) {
        // CTRL disables editing
        $('iframe')
            .keydown(function (e) {
                console.log(e.which)
                if(e.which == 17) $(this).find('body').prop('contenteditable', false);
            })
            .keyup(function (e) {
                if(e.which == 17) $(this).find('body').prop('contenteditable', true);
            });
        /**/
           
        // convert old textarea to new WYSIWYG
        if(NOTE.val() !== undefined){
            var obj = $.jStorage.get("online-bloknot") || "";
            if ( obj !== undefined ) {
                var t = /^\<.*\>$/g;
                if ( t.test(obj) === false ) {
                    obj = obj.replace(/$/mg,'<br/>');
                }
            }
            NOTE.val( obj );
        }
        /**/

        // save content in browser at all times
        NOTE.change(function(){
            if (timer) clearTimeout(timer);
            timer = setTimeout(function(){ save(); },10000);
        });
        $(window).unload(function(){ save(); });
        $('a').on('mousedown',function(e){ save(); return true; }); 
        /**/

        // download button
        $('a[href="#export]"').on('click',function(e){
            e.preventDefault();
            saveTextAsFile();
        });
        /**/

        // WYSIWYG itself
        $WYSIWYG = CKEDITOR.replace('note');
        
        $WYSIWYG.on('change',function(e){
                var ckvalue = this.getData();
                NOTE.val( ckvalue );
                NOTE.trigger('change');
            });
        $WYSIWYG.on('instanceReady', function(ev) {
            //catch ctrl+clicks on <a>'s in edit mode to open hrefs in new tab/window
            $('iframe.cke_wysiwyg_frame').contents().keypress(function(e) {
                //console.log('contentDom', e.currentTarget.activeElement.lastChild);
                if(e.keyCode==32){
                   // $('.cke_button_on').click();
                }else{

                }
            });
            $('iframe.cke_wysiwyg_frame').contents().click(function(e) {
                //console.log(e.target.href);
                if(typeof e.target.href != 'undefined' ) { //&& e.ctrlKey == true
                    //alert('hover')
                    window.open(e.target.href, 'new' + e.screenX);
                }
            });
            $('iframe.cke_wysiwyg_frame').contents().find('*')//.find(':active').parents('.cke_contents').css('border-color','#66afe9')
                .focus(function(){
                    $('.cke_contents').addClass('cke_active');//.css('borderColor','#66afe9');
                })
                .blur(function() {
                    $('.cke_contents').removeClass('cke_active');
                })
        });
        /**/
        
        // disable "link" confirm cancel
        CKEDITOR.on('dialogDefinition', function(dialogDefinitionEvent) {
            if (dialogDefinitionEvent.data.name == 'link') {
                var dialogDefinition = dialogDefinitionEvent.data.definition;
                dialogDefinition.dialog.on('cancel', function(cancelEvent) {
                    return false;
                }, this, null, -1);
            }
        });
        /**/
        
        // Adaptive height
        $(window).on('resize', function(e){
            $WYSIWYG.resize(null, getNoteHeight() + 40);
        });
        /**/
    }
    
            
        /* spoilers */
        $('.spoiler').each(function() {
            var that = $(this).next('.spoilermore');
            that.css('display', 'none');
            $(this).on('click', function(e) {
                e.preventDefault();
                that.slideToggle();
                $(this).toggleClass('a');
            });
        }); 
        /**/
});
