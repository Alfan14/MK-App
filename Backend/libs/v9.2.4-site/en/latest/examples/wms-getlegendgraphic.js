"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[3578],{70453:function(e,t,n){var o=n(2091),s=n(41564),r=n(28e3),c=n(87240),a=n(12185),u=n(47085);const g=new o.A({url:"https://ahocevar.com/geoserver/wms",params:{LAYERS:"topp:states"},ratio:1,serverType:"geoserver"}),i=function(e){const t=g.getLegendUrl(e);document.getElementById("legend").src=t},w=[new a.A({source:new r.A}),new u.A({extent:[-13884991,2870341,-7455066,6338219],source:g})],l=new s.A({layers:w,target:"map",view:new c.Ay({center:[-10997148,4569099],zoom:4})}),p=l.getView().getResolution();i(p),l.getView().on("change:resolution",(function(e){const t=e.target.getResolution();i(t)}))}},function(e){var t;t=70453,e(e.s=t)}]);
//# sourceMappingURL=wms-getlegendgraphic.js.map