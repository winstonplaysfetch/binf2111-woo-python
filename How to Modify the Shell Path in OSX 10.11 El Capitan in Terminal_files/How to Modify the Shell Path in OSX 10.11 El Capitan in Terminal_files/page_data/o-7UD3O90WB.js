if (self.CavalryLogger) { CavalryLogger.start_js(["O8y59"]); }

__d('PagePluginEvents',['ImmutableObject','keyMirrorRecursive'],(function a(b,c,d,e,f,g){'use strict';if(c.__markCompiled)c.__markCompiled();var h=new (c('ImmutableObject'))(c('keyMirrorRecursive')({page_plugin:{tab:{configured:'',click:'',render:''},messages:{send:'',logged_out:'',invalid_height:''}}}));f.exports=h;}),null);
__d("XPagePluginLoggingController",["XController"],(function a(b,c,d,e,f,g){c.__markCompiled&&c.__markCompiled();f.exports=c("XController").create("\/platform\/plugin\/page\/logging\/",{});}),null);
__d('PagePluginLogger',['AsyncRequest','XPagePluginLoggingController'],(function a(b,c,d,e,f,g){'use strict';if(c.__markCompiled)c.__markCompiled();function h(i,j){this.$PagePluginLogger1=i;this.$PagePluginLogger2=j;}h.prototype.notify=function(i,j,k){var l=c('XPagePluginLoggingController').getURIBuilder().getURI();new (c('AsyncRequest'))().setURI(l).setMethod('POST').setData({event_name:i,page_id:this.$PagePluginLogger1,tab:j,data:Object.assign(k?k:{},{refererURL:this.$PagePluginLogger2})}).send();};f.exports=h;}),null);
__d('PluginTabItem.react',['cx','React'],(function a(b,c,d,e,f,g,h){'use strict';var i,j;if(c.__markCompiled)c.__markCompiled();i=babelHelpers.inherits(k,c('React').Component);j=i&&i.prototype;k.prototype.render=function(){var l=this.props.tab.key;return (c('React').createElement('div',{className:"_eg_"+(this.props.activeTabKey===l?' '+"_eh2":''),onClick:function(){return this.props.onSelected(l);}.bind(this)},c('React').createElement('div',{className:"_eh3"},this.props.tab.title)));};function k(){i.apply(this,arguments);}f.exports=k;}),null);
__d('PluginTabControl.react',['cx','Grid.react','PluginTabItem.react','React'],(function a(b,c,d,e,f,g,h){'use strict';var i,j;if(c.__markCompiled)c.__markCompiled();var k=c('Grid.react').GridItem;i=babelHelpers.inherits(l,c('React').Component);j=i&&i.prototype;l.prototype.render=function(){return (c('React').createElement(c('Grid.react'),{className:"_4v3l",cols:this.props.tabs.length,fixed:true},this.props.tabs.map(function(m){return (c('React').createElement(k,{className:"_4v3m",key:m.key},c('React').createElement(c('PluginTabItem.react'),{activeTabKey:this.props.activeTabKey,tab:m,onSelected:this.props.onTabSelected})));}.bind(this))));};function l(){i.apply(this,arguments);}f.exports=l;}),null);
__d("XPluginTabAsyncRendererController",["XController"],(function a(b,c,d,e,f,g){c.__markCompiled&&c.__markCompiled();f.exports=c("XController").create("\/platform\/plugin\/tab\/renderer\/",{});}),null);
__d('PluginTabFetcher.react',['csx','cx','AsyncRequest','DOM','DOMQuery','Event','React','ReactDOM','XPluginTabAsyncRendererController','XUISpinner.react'],(function a(b,c,d,e,f,g,h,i){'use strict';var j,k;if(c.__markCompiled)c.__markCompiled();j=babelHelpers.inherits(l,c('React').Component);k=j&&j.prototype;function l(m,n){k.constructor.call(this,m,n);this.state={isFetchingComponent:false,asyncContentLoaded:false};this.hasMoreContent=true;this.isLoadingContent=false;}l.prototype.componentWillReceiveProps=function(m){if(m.isActive===this.props.isActive||!m.isActive)return;this.$PluginTabFetcher1();};l.prototype.componentDidMount=function(){if(this.props.isActive)this.$PluginTabFetcher1();};l.prototype.$PluginTabFetcher2=function(){var m=this.refs.container,n=m.clientHeight,o=m.children[0].clientHeight,p=m.scrollTop,q=100;if(!this.isLoadingContent&&this.hasMoreContent&&p+n+q>o){this.isLoadingContent=true;this.$PluginTabFetcher3();}};l.prototype.$PluginTabFetcher3=function(){var m=c('XPluginTabAsyncRendererController').getURIBuilder().getURI(),n=this.props.tab.configData;new (c('AsyncRequest'))().setURI(m).setMethod('POST').setData({cursor:this.cursor,config_json:JSON.stringify(n),key:this.props.tab.key}).setHandler(function(o){this.setState({isFetchingComponent:false,asyncContentLoaded:true},function(){var p=o.payload;this.isLoadingContent=false;if(this.hasMoreContent){var q=c('DOMQuery').scry(this.refs.container,"._1_lk"),r=q[q.length-1];c('DOM').appendContent(r,p.content.markup);}}.bind(this));}.bind(this)).send();};l.prototype.$PluginTabFetcher4=function(){this.scrollListener=c('Event').listen(this.refs.container,'scroll',function(){if(this.scrollTimeout){clearTimeout(this.scrollTimeout);this.scrollTimeout=null;}this.scrollTimeout=setTimeout(function(){return this.$PluginTabFetcher2();}.bind(this),250);}.bind(this));var m=c('DOMQuery').find(this.refs.container,"._10b6");c('Event').listen(m,'noMoreContent',function(){this.hasMoreContent=false;this.scrollListener.remove();}.bind(this));c('Event').listen(m,'setCursor',function(n){this.cursor=n.getData();}.bind(this));};l.prototype.$PluginTabFetcher1=function(){if(!this.state.asyncContentLoaded&&!this.state.isFetchingComponent){this.setState({isFetchingComponent:true});var m=c('XPluginTabAsyncRendererController').getURIBuilder().getURI();new (c('AsyncRequest'))().setURI(m).setMethod('POST').setData({config_json:JSON.stringify(this.props.tab.configData),key:this.props.tab.key}).setHandler(function(n){this.setState({isFetchingComponent:false,asyncContentLoaded:true},function(){var o=n.payload;c('DOM').setContent(c('ReactDOM').findDOMNode(this.refs.container),o.content.markup);if(this.props.tab.canLoadMore){this.cursor='';this.$PluginTabFetcher4();}}.bind(this));}.bind(this)).send();}};l.prototype.render=function(){return (c('React').createElement('div',{className:!this.props.isActive?"hidden_elem":''},c('React').createElement('div',{style:{maxHeight:this.props.tabHeight+'px'},className:"_10b4"+(this.state.isFetchingComponent?' '+"hidden_elem":''),ref:'container'}),c('React').createElement('div',{className:"_10b5"+(!this.state.isFetchingComponent?' '+"hidden_elem":'')},c('React').createElement(c('XUISpinner.react'),{className:"_4g7o",size:'large'}))));};f.exports=l;}),null);
__d('PluginTabContainer.react',['cx','PluginTabControl.react','PluginTabFetcher.react','React'],(function a(b,c,d,e,f,g,h){'use strict';var i,j;if(c.__markCompiled)c.__markCompiled();i=babelHelpers.inherits(k,c('React').Component);j=i&&i.prototype;function k(l,m){j.constructor.call(this,l,m);this.state={activeTabKey:this.props.activeTabKey};}k.prototype.componentDidMount=function(){this.props.tabs.map(function(l){return this.onTabLoaded(l);}.bind(this));};k.prototype.onTabLoaded=function(l){};k.prototype.onTabSelected=function(l){this.setState({activeTabKey:l});};k.prototype.render=function(){var l=this.props.tabs.length;if(l===0)return null;return (c('React').createElement('div',null,l>1?c('React').createElement(c('PluginTabControl.react'),{tabs:this.props.tabs,activeTabKey:this.state.activeTabKey,onTabSelected:function(m){return this.onTabSelected(m);}.bind(this)}):null,c('React').createElement('div',{className:"_2hkj"},this.props.tabs.map(function(m){return (c('React').createElement(c('PluginTabFetcher.react'),{key:m.key,tab:m,isActive:m.key===this.state.activeTabKey,tabHeight:this.props.tabHeight}));}.bind(this)))));};f.exports=k;}),null);
__d('PagePluginTabContainer.react',['PagePluginEvents','PagePluginLogger','PluginTabContainer.react'],(function a(b,c,d,e,f,g){'use strict';var h,i;if(c.__markCompiled)c.__markCompiled();h=babelHelpers.inherits(j,c('PluginTabContainer.react'));i=h&&h.prototype;function j(k,l){i.constructor.call(this,k,l);this.$PagePluginTabContainer1=new (c('PagePluginLogger'))(k.pageID,k.refererURI);}j.prototype.onTabLoaded=function(k){this.$PagePluginTabContainer1.notify(c('PagePluginEvents').page_plugin.tab.configured,k.key);};j.prototype.onTabSelected=function(k){this.$PagePluginTabContainer1.notify(c('PagePluginEvents').page_plugin.tab.click,k);i.onTabSelected.call(this,k);};f.exports=j;}),null);