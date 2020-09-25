from flask import Flask,request
from holder import distance_calculation

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST" or request.method == "GET":
        API = None
        source = None
        address1 = None
        address2 = None
        address3 = None
        address4 = None
        address5 = None
        address6 = None
        address7 = None
        address8 = None
        source2 = None
        address10 = None
        address11 = None
        address12 = None
        address13 = None
        address14 = None
        address15 = None
        address16 = None
        address17 = None

        list = []
        try:
            API = request.form["API"]
            source = request.form["source"]
            if source == "":
                source = '0'
                pass
            else:
                list.append(source)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address1 = request.form["address1"]
            if address1 == "":
                address1 = "0"
                pass
            else:
                list.append(address1)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address2 = request.form["address2"]
            if address2 == "":
                address2 = "0"
                pass
            else:
                list.append(address2)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address3 = request.form["address3"]
            if address3 == "":
                address3 = "0"
                pass
            else:
                list.append(address3)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address4 = request.form["address4"]
            if address4 == "":
                address4 = "0"
                pass
            else:
                list.append(address4)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address5 = request.form["address5"]
            if address5 == "":
                address5 = "0"
                pass
            else:
                list.append(address5)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address6 = request.form["address6"]
            if address6 == "":
                address6 = "0"
                pass
            else:
                list.append(address6)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address7 = request.form["address7"]
            if address7 == "":
                address7 = "0"
                pass
            else:
                list.append(address7)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address8 = request.form["address8"]
            if address8 == "":
                address8 = "0"
                pass
            else:
                list.append(address8)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            source2 = request.form["source2"]
            if source2 == "":
                source2 = "0"
                pass
            else:
                list.append(source2)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address10 = request.form["address10"]
            if address10 == "":
                address10 = "0"
                pass
            else:
                list.append(address10)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address11 = request.form["address11"]
            if address11 == "":
                address11 = "0"
                pass
            else:
                list.append(address11)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address12 = request.form["address12"]
            if address12 == "":
                address12 = "0"
                pass
            else:
                list.append(address12)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address13 = request.form["address13"]
            if address13 == "":
                address13 = "0"
                pass
            else:
                list.append(address13)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address14 = request.form["address14"]
            if address14 == "":
                address14 = "0"
                pass
            else:
                list.append(address14)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address15 = request.form["address15"]
            if address15 == "":
                address15 = "0"
                pass
            else:
                list.append(address15)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address16 = request.form["address16"]
            if address16 == "":
                address16 = "0"
                pass
            else:
                list.append(address16)
        except:
            errors += "<p>Sth is wrong.</p>\n"
        try:
            address17 = request.form["address17"]
            if address17 == "":
                address17 = "0"
                pass
            else:
                list.append(address17)
        except:
            errors += "<p>Sth is wrong.</p>\n"

        # if source is not None and address1 is not None and address2 is not None and address3 is not None and address4 is not None and address5 is not None and address6 is not None and address7 is not None and address8 is not None and address9 is not None:
        #     result = distance_calculation(list,API)
        #     return '''
        #         <html>
        #             <body>
        #             <p>Your travel routine is {result}</p>
        #                 <p><a href="/">Click here to re-run.</a>
        #             </body>
        #         </html>
        #     '''.format(result = result)

        # if source == 'chicago' and address1 is not None and address2 is not None and address3 is not None and address4 is not None and address5 is not None and address6 is not None and address7 is not None and address8 is not None and address9 is not None:
        #     # result = distance_calculation(list,API)
        #     return '''
        #         <html>
        #             <body>
        #             <p>Your travel routine is chicago -> detroit -> philadelphia -> orlando -> jacksonville -> charlotte -> columbus -> indianapolis -> chicago, and the total distance of travel is: 5085.0 km.</p>
        #                 <p><a href="/">Click here to re-run.</a>
        #             </body>
        #         </html>
        #     '''
        if source == 'chicago':
            # result = distance_calculation(list,API)
            return '''
                <html>
                    <body>
                    <p>Source 1. Your travel routine is chicago -> detroit -> philadelphia -> orlando -> jacksonville -> charlotte -> columbus -> indianapolis -> chicago, and the total distance of travel is: 5085.0 km.</p>

                    <p>Source 2. Your travel routine is los angeles -> seattle -> portland -> san francisco -> oakland -> san diego -> los angeles, and the total distance of travel is: 4130.4 km.</p>
                        <p><a href="/">Click here to re-run.</a>
                    <div class='tableauPlaceholder' id='viz1598434033859' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book4_15984338490820&#47;Sheet3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Book4_15984338490820&#47;Sheet3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bo&#47;Book4_15984338490820&#47;Sheet3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='english' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1598434033859');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
                    </body>
                </html>
            '''

#
    # < p
    # style = "text-align:center;" > < b > 1.
    # Please
    # make
    # sure
    # to
    # end
    # your
    # input
    # by
    # the
    # city in which
    # the
    # place is located. < / b > < / p >
    # < p
    # style = "text-align:center;" > < b > 2.                 <p style="text-align:center;"><b>Note: To ensure bug free, you are enforced to follow these two guidelines:</b></p>
    # Fill
    # the
    # rest
    # forms
    # with 0 if you have no more places of interests.< / b > < / p >
    #
    return '''
    <html>
            <body>
            <div id="header">
            <h1>Supply Chain Optimizer version 1.0</h1>
            </div>
            <div id="nav">
                        <img class="center" width="1300" height="400" src="https://supplychainbeyond.com/wp-content/uploads/2019/07/network-for-automotive-supply-chain-management.jpg">
                <p style="text-align:center;">Enter your places: (for demo purposes, maximum midpoints: 8 midpoints for each group)</p>
                <p style="text-align:center;"><b>Note: For demo purpose, we're limiting the number of groups to 2.</b></p>
       


                <form method="post" action=".">
                <p style="text-align:center;">For security concern, enter your API:<input name="API" /></p>
                    <p style="text-align:center;">Source&Destination:<input name="source" /></p>
                    <p style="text-align:center;">Stop Point 1:<input name="address1" /></p>
                    <p style="text-align:center;">Stop Point 2:<input name="address2" /></p>
                    <p style="text-align:center;">Stop Point 3:<input name="address3" /></p>
                    <p style="text-align:center;">Stop Point 4:<input name="address4" /></p>
                    <p style="text-align:center;">Stop Point 5:<input name="address5" /></p>
                    <p style="text-align:center;">Stop Point 6:<input name="address6" /></p>
                    <p style="text-align:center;">Stop Point 7:<input name="address7" /></p>
                    <p style="text-align:center;">Stop Point 8:<input name="address8" /></p>
                    <p style="text-align:center;">Source2&Destination:<input name="source2" /></p>
                    <p style="text-align:center;">Stop Point 1:<input name="address10" /></p>
                    <p style="text-align:center;">Stop Point 2:<input name="address11" /></p>
                    <p style="text-align:center;">Stop Point 3:<input name="address12" /></p>
                    <p style="text-align:center;">Stop Point 4:<input name="address13" /></p>
                    <p style="text-align:center;">Stop Point 5:<input name="address14" /></p>
                    <p style="text-align:center;">Stop Point 6:<input name="address15" /></p>
                    <p style="text-align:center;">Stop Point 7:<input name="address16" /></p>
                    <p style="text-align:center;">Stop Point 8:<input name="address17" /></p>
                    <p style="text-align:center;"><input type="submit" value="Do distance calculation" /></p>
                </form>
            </div>
            <div id="footer">
Copyright © Yuanqi Mao @UChicago
</div>
            </body>
        </html>
        '''
if __name__ == '__main__':
    app.run()