from PDFReportGenerator import PDFReportGenerator

def present_tuples_simple(tuples):
    for tuple in tuples:
        print(tuple)
        
def report_to_pdf(report_title, headers, tuples):
    pdf = PDFReportGenerator(report_title)
    
    print('Exporting PDF...')
    pdf.report(headers, tuples, report_title + '.pdf')
    print('PDF exported successfully!')