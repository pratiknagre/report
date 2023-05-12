import file
def generate_report():
    report_content="This is a sample report."
# save the report to a file
    with open('report.txt','w') as f :
        f.write(report_content)

def export_report_to-s3():
# setup the s3 client
s3=boto3.client('s3')
with open ('report.txt','rb') as f :
    s3.upload_fileobj(f,'my-s3-bucket','reports/report.txt')
