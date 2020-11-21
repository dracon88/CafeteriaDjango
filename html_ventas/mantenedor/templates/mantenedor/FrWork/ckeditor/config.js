/**
 * @license Copyright (c) 2003-2014, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */
//http://pierrebaron.fr/PBCKCode/demo-syntax-highlighter.html
CKEDITOR.editorConfig = function( config ) {
  //config.protectedSource.push(/<\?[\s\S]*?\?>/g); // PHP Code
  //config.protectedSource.push(/<pre[\s\S]*?\pre>/g); // pre tag
  //config.protectedSource.push(/<activity[\s\S]*?\activity>/g); // pre tag
  //config.protectedSource.push(/<code[\s\S]*?\code>/g); // code tag
  //config.extraPlugins = '';
  
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.language = 'es';
	//config.uiColor = '#f9f9f9';
	//config.skin = 'kama';
	//config.enterMode = CKEDITOR.ENTER_BR;
	config.colorButton_colors = '4A5A73,c54747,00773d,555555';
	config.height = '350px';
	//config.width = '600px';
	//config.resize_enabled = false;
	
	//config.extraPlugins = 'insertpre,pbckcode';
	config.extraPlugins = 'insertpre';
	config.insertpre_class = 'prettyprint';
	config.insertpre_style = 'background-color:#F8F8F8;border:1px solid #DDD;padding:10px;';
	//config.htmlEncodeOutput = false;
    //config.entities = false;
	//config.toolbarGroups = [
    //    // shows the source button
    //    { name: 'document', groups: [ 'mode'] },
    //    // shows the pbckcode button
    //    { name: 'pbckcode' }
    //];
    //config.extraPlugins = 'pbckcode,onchange';
	//config.extraPlugins += ',pbckcode';
    //config.pbckcode = {
    //    modes :  [ ["Java" , "java"], ["Markdown" , "markdown"] ],
    //    highlighter : "HIGHLIGHT"
    //};	
	



	//config.extraPlugins = 'syntaxhighlight';
	//config.extraPlugins += (config.extraPlugins ? ',syntaxhighlight' : 'syntaxhighlight' );
	//config.toolbar_Full.push(['Code']);
	//config.toolbar_DrupalFull = [
  //['Source'],
  //...
  //['DrupalBreak', 'DrupalPageBreak','Code']
//];

};
/*
CKEDITOR.on( 'instanceReady', function( ev ) {

var blockTags = ['pre'];
var rules = {
	indent : true,
	breakBeforeOpen : true,
	breakAfterOpen : true,
	breakBeforeClose : true,
	breakAfterClose : true
};

for (var i=0; i<blockTags.length; i++) {
ev.editor.dataProcessor.writer.setRules( blockTags[i], rules );
}

}); 
*/