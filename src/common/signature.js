

function asd() {
    function e(e, a, r) {
        return (b[e] || (b[e] = t("x,y", "return x " + e + " y")))(r, a)
    }
    function a(e, a, r) {
        return (k[r] || (k[r] = t("x,y", "return new x[y](" + Array(r + 1).join(",x[++y]").substr(1) + ")")))(e, a)
    }
    function r(e, a, r) {
        var n, t, s = {}, b = s.d = r ? r.d + 1 : 0;
        for (s["$" + b] = s,
        t = 0; t < b; t++)
            s[n = "$" + t] = r[n];
        for (t = 0,
        b = s.length = a.length; t < b; t++)
            s[t] = a[t];
        return c(e, 0, s)
    }
    function c(t, b, k) {
        function u(e) {
            v[x++] = e
        }
        function f() {
            return g = t.charCodeAt(b++) - 32,
            t.substring(b, b += g)
        }
        function l() {
            try {
                y = c(t, b, k)
            } catch (e) {
                h = e,
                y = l
            }
        }
        for (var h, y, d, g, v = [], x = 0; ; )
            switch (g = t.charCodeAt(b++) - 32) {
            case 1:
                u(!v[--x]);
                break;
            case 4:
                v[x++] = f();
                break;
            case 5:
                u(function(e) {
                    var a = 0
                      , r = e.length;
                    return function() {
                        var c = a < r;
                        return c && u(e[a++]),
                        c
                    }
                }(v[--x]));
                break;
            case 6:
                y = v[--x],
                u(v[--x](y));
                break;
            case 8:
                if (g = t.charCodeAt(b++) - 32,
                l(),
                b += g,
                g = t.charCodeAt(b++) - 32,
                y === c)
                    b += g;
                else if (y !== l)
                    return y;
                break;
            case 9:
                v[x++] = c;
                break;
            case 10:
                u(s(v[--x]));
                break;
            case 11:
                y = v[--x],
                u(v[--x] + y);
                break;
            case 12:
                for (y = f(),
                d = [],
                g = 0; g < y.length; g++)
                    d[g] = y.charCodeAt(g) ^ g + y.length;
                u(String.fromCharCode.apply(null, d));
                break;
            case 13:
                y = v[--x],
                h = delete v[--x][y];
                break;
            case 14:
                v[x++] = t.charCodeAt(b++) - 32;
                break;
            case 59:
                u((g = t.charCodeAt(b++) - 32) ? (y = x,
                v.slice(x -= g, y)) : []);
                break;
            case 61:
                u(v[--x][t.charCodeAt(b++) - 32]);
                break;
            case 62:
                g = v[--x],
                k[0] = 65599 * k[0] + k[1].charCodeAt(g) >>> 0;
                break;
            case 65:
                h = v[--x],
                y = v[--x],
                v[--x][y] = h;
                break;
            case 66:
                u(e(t[b++], v[--x], v[--x]));
                break;
            case 67:
                y = v[--x],
                d = v[--x],
                u((g = v[--x]).x === c ? r(g.y, y, k) : g.apply(d, y));
                break;
            case 68:
                u(e((g = t[b++]) < "<" ? (b--,
                f()) : g + g, v[--x], v[--x]));
                break;
            case 70:
                u(!1);
                break;
            case 71:
                v[x++] = n;
                break;
            case 72:
                v[x++] = +f();
                break;
            case 73:
                u(parseInt(f(), 36));
                break;
            case 75:
                if (v[--x]) {
                    b++;
                    break
                }
            case 74:
                g = t.charCodeAt(b++) - 32 << 16 >> 16,
                b += g;
                break;
            case 76:
                u(k[t.charCodeAt(b++) - 32]);
                break;
            case 77:
                y = v[--x],
                u(v[--x][y]);
                break;
            case 78:
                g = t.charCodeAt(b++) - 32,
                u(a(v, x -= g + 1, g));
                break;
            case 79:
                g = t.charCodeAt(b++) - 32,
                u(k["$" + g]);
                break;
            case 81:
                h = v[--x],
                v[--x][f()] = h;
                break;
            case 82:
                u(v[--x][f()]);
                break;
            case 83:
                h = v[--x],
                k[t.charCodeAt(b++) - 32] = h;
                break;
            case 84:
                v[x++] = !0;
                break;
            case 85:
                v[x++] = void 0;
                break;
            case 86:
                u(v[x - 1]);
                break;
            case 88:
                h = v[--x],
                y = v[--x],
                v[x++] = h,
                v[x++] = y;
                break;
            case 89:
                u(function() {
                    function e() {
                        return r(e.y, arguments, k)
                    }
                    return e.y = f(),
                    e.x = c,
                    e
                }());
                break;
            case 90:
                v[x++] = null;
                break;
            case 91:
                v[x++] = h;
                break;
            case 93:
                h = v[--x];
                break;
            case 0:
                return v[--x];
            default:
                u((g << 16 >> 16) - 16)
            }
    }
    var n = this
      , t = n.Function
      , s = Object.keys || function(e) {
        var a = {}
          , r = 0;
        for (var c in e)
            a[r++] = c;
        return a.length = r,
        a
    }
      , b = {}
      , k = {};
    r(String.fromCharCode(103,114,36,68,97,116,101,110,32,1048,98,47,115,33,108,32,121,850,121,313,103,44,40,108,102,105,126,97,104,96,123,109,118,44,45,110,124,106,113,101,119,86,120,112,123,114,118,109,109,120,44,38,101,102,102,127,107,120,91,33,99,115,34,108,34,46,80,113,37,119,105,100,116,104,108,34,64,113,38,104,101,105,103,104,116,108,34,118,114,42,103,101,116,67,111,110,116,101,120,116,120,36,34,50,100,91,33,99,115,35,108,35,44,42,59,63,124,117,46,124,117,99,123,117,113,36,102,111,110,116,108,35,118,114,40,102,105,108,108,84,101,120,116,120,36,36,40856,3601,3616,44221,50,60,91,35,99,125,108,35,50,113,42,115,104,97,100,111,119,66,108,117,114,108,35,49,113,45,115,104,97,100,111,119,79,102,102,115,101,116,88,108,35,36,36,108,105,109,101,113,43,115,104,97,100,111,119,67,111,108,111,114,108,35,118,114,35,97,114,99,120,56,56,56,48,50,91,37,99,125,108,35,118,114,38,115,116,114,111,107,101,120,91,32,99,125,108,34,118,44,41,125,101,79,109,121,111,90,66,93,109,120,91,32,99,115,33,48,115,36,108,36,80,98,60,107,55,108,32,108,33,114,38,108,101,110,103,116,104,98,37,94,108,36,49,43,115,36,106,2,108,32,32,115,35,105,36,49,101,107,49,115,36,103,114,35,116,97,99,107,52,41,122,103,114,35,116,97,99,36,33,32,43,48,111,33,91,35,99,106,63,111,32,93,33,108,36,98,37,115,34,111,32,93,33,108,34,108,36,98,42,98,94,48,100,35,62,62,62,115,33,48,115,37,121,65,48,115,34,108,34,108,33,114,38,108,101,110,103,116,104,98,60,107,43,108,34,94,108,34,49,43,115,34,106,5,108,32,32,115,38,108,38,122,48,108,33,36,32,43,91,34,99,115,39,40,48,108,35,105,39,49,112,115,57,119,120,98,38,115,40,41,32,38,123,115,41,47,115,40,103,114,38,83,116,114,105,110,103,114,44,102,114,111,109,67,104,97,114,67,111,100,101,115,41,48,115,42,121,87,108,32,46,95,98,38,115,32,111,33,93,41,108,32,108,32,74,98,60,107,36,46,97,106,59,108,32,46,84,98,60,107,36,46,103,106,47,108,32,46,94,98,60,107,38,105,34,45,52,106,33,31,43,38,32,115,43,121,80,111,33,93,43,115,33,108,33,108,32,72,100,62,38,108,33,108,32,66,100,62,38,43,108,33,108,32,60,100,62,38,43,108,33,108,32,54,100,62,38,43,108,33,108,32,38,43,32,115,44,121,61,111,33,111,33,93,47,113,34,49,51,111,33,108,32,113,34,49,48,111,33,93,44,108,32,50,100,62,38,32,115,46,123,115,45,121,77,111,33,111,33,93,48,113,34,49,51,111,33,93,42,76,100,60,108,32,52,100,35,62,62,62,98,124,115,33,111,33,108,32,113,34,49,48,111,33,93,44,108,33,38,32,115,47,121,73,111,33,111,33,93,46,113,34,49,51,111,33,93,44,111,33,93,42,74,100,60,108,32,54,100,35,62,62,62,98,124,38,111,33,93,43,108,32,38,43,32,115,48,108,45,108,33,38,108,45,108,33,105,39,49,122,49,52,49,122,52,98,47,64,100,60,108,34,98,124,38,43,108,45,108,40,108,33,98,94,38,43,108,45,108,38,122,108,39,103,44,41,103,107,125,101,106,111,123,127,99,109,44,41,124,121,110,126,76,105,106,126,101,109,91,34,99,108,36,98,37,64,100,60,108,38,122,108,39,108,32,36,32,43,91,34,99,108,36,98,37,98,124,38,43,108,45,108,37,56,100,60,64,98,124,108,33,98,94,38,43,32,113,36,115,105,103,110,32), [TAC = {}]);
}

var e = function(a){
    var r = {
        exports: {},
        id: a,
        loaded: !1,
    };
    return asd.call()
};

asd();

var get_signature = function (hot_time, ua) {
    global.navigator = {
        userAgent: ua
    };
    var a = 299;
    var tac = e(a);
    return TAC.sign(hot_time);
};


function  get_sign(userID,max_behot_time) {
    global.navigator = {};
    global.navigator.userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36";
    Function(function(e) {
    return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(i) {
        return e[15 & i.charCodeAt(0)]
    })
}("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [TAC = {}]);
;
    if (userID===''){
        strr = max_behot_time;}
    else{
        if (max_behot_time===''){
            strr = userID;
        }
        else {
            strr = userID+''+max_behot_time;
        }

    }
    var data = TAC.sign(strr);
    return data
}


function sign_u(media_id) {
    global.navigator = {};
    global.navigator.userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36";
    Function(function(e) {
    return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function(i) {
        return e[15 & i.charCodeAt(0)]
    })
}("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [TAC = {}]);
;
    var data = TAC.sign(media_id);
    return data
}
