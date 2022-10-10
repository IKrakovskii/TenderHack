import aspose.words as aw

doc = aw.Document('Data/ПРЕДЛОЖЕНИЕ УЧАСТНИКА ОТКРЫТОГО ЗАПРОСА КОТИРОВОК.pdf')
doc.save('Data/Output.docx')