import sys
import getopt

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <title>Report Generation Tool</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>

<nav class="navbar navbar-default">
    <div><br></div>
    <div class="container-fluid">
        <ul>
            <div class="navbar-header">
                <a class="navbar-brand">Generated Report </a>
            </div>
            <br>
            <br>
        </ul>
    </div>
</nav>

<table cellpadding="0" cellspacing="0" border="0" align="center" width="100%" id="navbar-table">
            <table cellspacing="0" cellpadding="0" border="0" align="center" width="100%">
                <tr style="max-width: 100%;">

                Below you will find the report generation results!

                <br>
                <br>

                <table class="table table-condensed table-striped table-hover table-bordered">
                            <thead>
                            <tr>
                                <th class="col-xs-10">Line</th>
                                <th class="col-xs-2">Pass/Fail</th>
                            </tr>
                            </thead>
                            <tbody>
                            {}
                            </tbody>
                </table>


                    <td style="width: 88%; font-size: 1.5em; color: #777777; padding-right: 20px;" valign="middle"
                        align="right"></td>
                </tr>
            </table>
</table>
</body>
</html>"""

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print 'generate_report.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '\n Command must meet following format. Your input file must be present inside the root of the project.' \
                  ' \n > python generate_report.py -i <inputfile.txt> -o <outputfile.html> \n'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    f = open(inputfile, 'r')
    report_as_array = f.readlines()

    finalized_report = []
    html_report = ""

    for line in report_as_array:
        if 'pass' in line.lower():
            finalized_report.append({'report_line': line,
                                     'classification': 'bg-success',
                                     'display': 'SUCCESS'})
        elif 'fail' in line.lower():
            finalized_report.append({'report_line': line,
                                     'classification': 'bg-danger',
                                     'display': 'FAIL'})
        else:
            finalized_report.append({'report_line': line,
                                     'classification': 'text-muted',
                                     'display': 'NONE'})

    for entry in finalized_report:
        # table_row = "<tr>{}{}</tr>"
        line_data = '<td width="60%">{}</td>'.format(entry['report_line'])
        classification_data = '<td width="30%" class={}>{}</td>'.format(entry['classification'], entry['display'])

        table_row = "<tr>" + line_data + classification_data + "</tr>"

        html_report += table_row

    finalized_html = html_template.format(html_report)

    text_file = open(outputfile, "w")
    text_file.write(finalized_html)
    text_file.close()

    print '>>> Your report has been successfully generated as {}!'.format(outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
