import pdfkit

class PDFReportGenerator:
    __WKHTMLTOPDF_PATH = 'tools\\wkhtmltopdf32.exe'

    # Export in own file and load @ runtime?
    __base_html = """
<html>
    <head>
        <title>$$REPORT_TITLE$$</title>
        <style>
            table, tr, th {
                font-family: 'Courier New';
                font-size: 24fr;
                border-bottom: 1px solid;
                border-color: darkgrey;
                width: 100%;
                text-align: center;
                border-collapse: collapse;
            }
            th {
                background-color: gray;
                color: white;
            }

            td {
                background-color: white;
                border-bottom: 1px solid;
                border-color: darkgrey;
            }
        </style>
    </head>
    <body>
        <h1>$$REPORT_TITLE$$</h1>
        <table>
            <tr>
                $$TABLE_HEADERS$$
            </tr>
"""

    def __init__(self, title):
        self.__pdf_config = pdfkit.configuration(wkhtmltopdf=self.__WKHTMLTOPDF_PATH)
        self.__report_title = title
        
    def __generate_html(self, headers, tuples):
        
        htmlstring = self.__base_html.replace('$$REPORT_TITLE$$', self.__report_title)
        
        headers_html = ''
        for header in headers:
            headers_html += '<th>{}</th>\n'.format(header)
        
        htmlstring = htmlstring.replace('$$TABLE_HEADERS$$', headers_html)
        
        for product in tuples:
            htmlstring += '<tr>\n'
            for product_field in product:
               htmlstring += '<td>{}</td>'.format(product_field)
            htmlstring += '\n</tr>\n'
        
        htmlstring += '</table></body></html>'
        
        return htmlstring
    
    def report(self, headers, tuples, file_out):
        pdfkit.from_string(self.__generate_html(headers, tuples), 
                           file_out, configuration=self.__pdf_config)