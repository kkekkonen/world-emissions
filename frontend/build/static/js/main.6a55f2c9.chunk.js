(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{27:function(e,t,a){e.exports=a(80)},35:function(e,t,a){},80:function(e,t,a){"use strict";a.r(t);var n=a(0),o=a.n(n),i=a(24),s=a.n(i),r=(a(33),a(35),a(11)),c=a(12),l=a(14),m=a(13),u=a(15),p=a(26),h=a(9),d=a(25),f=a.n(d);h.b.addAdapter(f.a);var v=function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(l.a)(this,Object(m.a)(t).call(this,e))).setPerCapita=function(e){var t=e.target,n="checkbox"===t.type?t.checked:t.value;a.processNation(a.state.nation.name,n)},a.findArrayElement=function(e,t){return t===e.name},a.selectNation=function(e){a.processNation(e.target.value,a.state.perCapita)},a.selectPrimaryNation=function(e){var t=a.state.countryData.find(function(t){return t.name===e.target.value});a.setState({nation:t})},a.selectNationToCompare=function(e){var t=a.state.countryData.find(function(t){return t.name===e.target.value});a.setState({nationToCompare:t})},a.processNation=function(e,t){var n=a.state.countryData.find(function(t){return t.name===e}),o={};if(t&&n)try{fetch("/country_population/"+n.Country_Code).then(function(e){return e.json()}).then(function(e){return Object.keys(e.data).map(function(t){n.data[t]&&e.data[t]&&(o[t]=n.data[t]/e.data[t])})}).then(function(){return a.setState({nation:Object(p.a)({},n,{data:o}),perCapita:t})})}catch(i){a.setState({nation:n,perCapita:t})}a.setState({nation:n,perCapita:t})},a.changeMode=function(e){a.setState({mode:e.target.value,nation:{},nationToCompare:{}})},a.processData=function(e){var t=[],n=[];e.forEach(function(e,a){t.push(e.name);var o=e.data[(new Date).getFullYear()-5];if(o)if(n.length<10)n.push({name:e.name,data:e.data,emissions:e.data[(new Date).getFullYear()-5]});else{var i=n.reduce(function(e,t){return t.emissions<e.emissions?t:e},n[0]);o>i.emissions&&(n.splice(n.indexOf(i),1),n.push({name:e.name,data:e.data,emissions:e.data[(new Date).getFullYear()-5]}))}}),a.setState({countryData:e,topEmissions:n,nations:t})},a.state={mode:"",countryData:[],topEmissions:[],nations:[],nation:{},nationToCompare:{},perCapita:!1},a}return Object(u.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=this;try{fetch("/emission_json").then(function(e){return e.json()}).then(function(t){return e.processData(t)})}catch(t){console.warn(t)}}},{key:"render",value:function(){return o.a.createElement("div",{className:"App"},o.a.createElement("select",{onChange:this.changeMode},o.a.createElement("option",{value:""}," select mode "),o.a.createElement("option",{value:"nation"},"nation"),o.a.createElement("option",{value:"compare nations"},"compare nations"),o.a.createElement("option",{value:"top emissions"},"top emissions")),"nation"===this.state.mode&&o.a.createElement("div",null,o.a.createElement("select",{onChange:this.selectNation},o.a.createElement("option",{value:""},"select nation"),this.state.nations.map(function(e,t){return o.a.createElement("option",{value:e,key:t},e)}),"}"),o.a.createElement("label",null,"Show per capita"),o.a.createElement("input",{name:"perCapita",type:"checkbox",checked:this.state.perCapita,onChange:this.setPerCapita})),"compare nations"===this.state.mode&&o.a.createElement("div",null,o.a.createElement("select",{onChange:this.selectPrimaryNation},o.a.createElement("option",{value:""},"select nation 1"),this.state.nations.map(function(e,t){return o.a.createElement("option",{value:e,key:t},e)}),"}"),o.a.createElement("select",{onChange:this.selectNationToCompare},o.a.createElement("option",{value:""},"select nation 2"),this.state.nations.map(function(e,t){return o.a.createElement("option",{value:e,key:t+"#compare"},e)}),"}")),"top emissions"===this.state.mode&&o.a.createElement(h.a,{data:this.state.topEmissions}),"nation"===this.state.mode&&0!==Object.keys(this.state.nation).length&&o.a.createElement(h.a,{data:this.state.nation.data}),"compare nations"===this.state.mode&&0!==Object.keys(this.state.nation).length&&0!==Object.keys(this.state.nationToCompare).length&&o.a.createElement(h.a,{data:[this.state.nation,this.state.nationToCompare]}))}}]),t}(n.Component),E=function(e){function t(){return Object(r.a)(this,t),Object(l.a)(this,Object(m.a)(t).apply(this,arguments))}return Object(u.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return o.a.createElement("main",{className:"content"},o.a.createElement("h1",{className:"text-white text-uppercase text-center my-4"},"Todo app"),o.a.createElement("div",{className:"row "},o.a.createElement("div",{className:"col-md-6 col-sm-10 mx-auto p-0"},o.a.createElement("div",{className:"card p-3"},o.a.createElement("div",{className:""},o.a.createElement(v,null))))))}}]),t}(n.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));s.a.render(o.a.createElement(E,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[27,2,1]]]);
//# sourceMappingURL=main.6a55f2c9.chunk.js.map