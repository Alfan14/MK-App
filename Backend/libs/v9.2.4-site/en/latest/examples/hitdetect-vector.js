"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[7645],{67048:function(e,n,t){var o=t(49208),r=t(41564),c=t(23986),i=t(29810),s=t(87240);const a=new c.A({background:"#1a2b39",source:new i.A({url:"https://openlayers.org/data/vector/ecoregions.json",format:new o.A}),style:{"fill-color":["string",["get","COLOR_NNH"],"#eee"]}}),u=new r.A({layers:[a],target:"map",view:new s.Ay({center:[0,0],zoom:1})}),g=new c.A({source:new i.A,map:u,style:{"stroke-color":"rgba(255, 255, 255, 0.7)","stroke-width":2}});let l;const f=function(e){a.getFeatures(e).then((function(e){const n=e.length?e[0]:void 0,t=document.getElementById("info");e.length?t.innerHTML=n.get("ECO_NAME")+": "+n.get("NNH_NAME"):t.innerHTML="&nbsp;",n!==l&&(l&&g.getSource().removeFeature(l),n&&g.getSource().addFeature(n),l=n)}))};u.on("pointermove",(function(e){if(e.dragging)return;const n=u.getEventPixel(e.originalEvent);f(n)})),u.on("click",(function(e){f(e.pixel)}))}},function(e){var n;n=67048,e(e.s=n)}]);
//# sourceMappingURL=hitdetect-vector.js.map