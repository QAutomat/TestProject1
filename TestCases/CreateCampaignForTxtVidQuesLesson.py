'''
Created on 01-Mar-2018

@author: dattatraya
'''

import os.path
import time

from BaseTestClass import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

from CampaignPageElements import CampPage

class CreateCampaignForTxtVidQuesLesson:
    
    def createCampaignForLessonTextVideoQuestion(self,campaignTitle,campDescription,lessonName,actualSuccessMessage,minPassingScore,numberOfAttempts):
        elements=CampPage()
        
        wait=WebDriverWait(driver, 60)
        
        print "\n\nCreating Campaign"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.campaignButtonFromSideMenuXpath())))
        elements.campaignButtonFromSideMenu()
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))

        if elements.campaignsPageHeaderText()=="Campaigns":
            print "Campaigns page displayed"
        else:
            print "Campaigns page is not displayed"
            raise Exception
        
        
        print "Clicking on Create Campaign button"
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.createCampaignButtonXpath())))
        elements.createCampaignButton()
        
        
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.Camp_titleXpath())))
        print "Create Campaign page is displayed"
        
                  
        elements.titleTextField(campaignTitle)
        print "Title entered ::campTitle"
        
        elements.descriptionField(campDescription)
        print "Description entered ::campDescription"
        
        print "Adding Lesson"
        #Add lesson button
        elements.addlessonButton()
        
        #Waiting until first lesson in pop is displayed
        wait.until(EC.visibility_of_element_located((By.XPATH,elements.FirstLessonWaitXpath())))
        
        #Searching lesson by its name
        elements.searchLesson(lessonName)
        
        #Waiting until lesson displayed
        elements.waitUntilSearchedLessonDisplayed(lessonName)
        
        #selecting searched lesson
        elements.selectSearchedLesson(lessonName)
        
        #waiting until add to campaign button is click able
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.AddToCampaign_ButtonXpath())))
        
        #Clicking on Add to Campaign button
        elements.addToCampaignButton()
        
        #Verifying Added lesson is displayed in Grid
        print "\nVerifying Added lesson is displayed in Grid"
        if elements.firstLessonInGrid()==lessonName:
            print "Lesson displayed in grid"
        else:
            print "Lesson not displayed in grid"
            
        
        print "Making This campaign as Graded campaign"    
        elements.makeThisAsAGradedCampaign()
        
        elements.setMinimumPassingScore(minPassingScore)
        
        print "Setting maximum number of attempts"
        elements.setAMaxNoOfAttempts(numberOfAttempts)
        
        
        
        wait.until(EC.element_to_be_clickable((By.XPATH,elements.SaveAndExit_ButtonXpath())))
        #Clicking on save & exit button
        print "Clicking on save & exit button"
        elements.saveAndExitButton()
        
        #verifying success message
        print "\nVerifying success message"
        
        if elements.successMessage()==actualSuccessMessage:
            print "Message '"+actualSuccessMessage+"' is displayed"
        else:
            print "Success message is not displayed properly"
            raise Exception
        
        #Verifying campaign detail page is displayed
        print "\nVerifying campaign detail page is displayed"
        
        if elements.campaignDetailPageHeaderText()==campaignTitle:
            print "Campaign detail page is displayed"
        else:
            print "Campaign detail page is not displayed"
            raise Exception
        
        print "\n----Text Execution Completed----\n"
    
    
    def textCard(self,textCard):
        print "Text card"
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]").click()
        
        textCardelement=driver.find_element_by_xpath("//div[@class='text']/div/div[1]/div")
        
        #Entering Text in Text card 
        
        webdriver.ActionChains(driver).move_to_element(textCardelement).click().send_keys(textCard).perform()
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        #Verifying entered text is displaying text card
        print "Verifying entered text is displaying text card"
        
        textAfterEntering=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/span/span").text
        
        if textAfterEntering==textCard:
            print "Verified Text '"+textCard+"' is displayed in Text Card"
        else:
            print "Text not displayed in Text card"
            raise Exception
        
    def videoCard(self,videoPath,timeToUploadVideo):
        
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        #Clicking on Video card
        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        
        #Uploading Video
        print "Uploading Video"
        driver.find_element_by_css_selector('input[type="file"]').send_keys(videoPath)
        
        WebDriverWait(driver, timeToUploadVideo).until(EC.visibility_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")))
        
        videoContainerlocator_afterupload= driver.find_element_by_xpath("html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[1]/button")
        
        if(videoContainerlocator_afterupload.is_displayed()):
            
            print "Successfully uploaded the Video file"
            
        else:
            print "Failed to upload the Video file"
            raise Exception
    
    
    def questionCard(self,questionCard,ans1,ans2):
         
        wait=WebDriverWait(driver, 60)
        print "\nInserting Question card"
        print "Click on (+) icon"
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div/span").click()
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[5]/div[1]/div").click()
        
        print "Question card selected"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='question-answer-input-0']")))
        print "Entering question"
        questionArea=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/div/div/p/textarea")
        questionArea.send_keys(questionCard)
        print "Question entered ::"
        
        print "Entering first answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").send_keys(ans1)
        print "First Answer entered "
        print "Entering Second answer"
        driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").send_keys(ans2)
        print "Second Answer entered "
        
        

         
        
        print "\nVerifying All the data entered is displaying in fields"
        
        if questionArea.text==questionCard:
            print "Question ::"+questionCard
        else:
            print "Question is not displayed"
            raise Exception
        
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-0']").text==ans1:
            print "Answer 1 ::"+ans1
        else:
            print "Answer 1 is not displayed"
            raise Exception
        
        if driver.find_element_by_xpath(".//*[@id='question-answer-input-1']").text==ans2:
            print "Answer 2 ::"+ans2
        else:
            print "Answer 2 is not displayed"
            raise Exception
    
    
    def createLessonTxtVidQue(self,lessonName,textCard,videoPath,questionCard,ans1,ans2,timeToUploadVideo):
        
        
        print "\n\n----This Test case creates the Track with one lesson which contains Text, Video, Question card-----\n"
        wait=WebDriverWait(driver, 60)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/create/lessons']")))

        print "Clicking on Lessons button from side menu"
        driver.find_element_by_xpath("//a[@href='/create/lessons']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div[3]/div[2]/div/header/div/button")))
     
        print "Click on Create lesson button"
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[2]/div/header/div/button").click()
        
        print "Verifying Create new lesson tab is displayed"
        
        #assert "Create a new lesson"==driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text
        if driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text == "Create a new lesson":
            print("Create a new lesson tab is displayed")
        else:
            print ""
            raise Exception
        
        # self.assertEqual("Create a new lesson", driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/h3").text)

        
               
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div[2]/div/div/div[2]/div[2]/div")))

        
        print "Clicked on Blank lesson"
        driver.find_element_by_xpath("html/body/div[2]/div/div/div[2]/div[2]/div").click()
        
        print "Creating New lesson With one Text card"
        
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea")))

        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[2]/div/div/div/h1/textarea").send_keys(lessonName)
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saving...']")))
        wait.until(EC.visibility_of_element_located((By.XPATH,"//span[@class='lesson-editor-status' and .='Saved']")))
        
        print "Entered lesson name ::"+lessonName
        
        
        objfor=CreateCampaignForTxtVidQuesLesson()
        
        #Text Card
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        objfor.textCard(textCard)
        
        # Video card
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        objfor.videoCard(videoPath, timeToUploadVideo)
        
       
        
        #Question card
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        objfor.questionCard(questionCard, ans1, ans2)
        
       
        
        print "All Cards inserted"
        
        
        print "Publishing lesson"

        publishbutton=wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/button")))
        
        driver.execute_script("arguments[0].click();",publishbutton)

        wait.until(EC.visibility_of_element_located((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))
        wait.until(EC.element_to_be_clickable((By.XPATH,"html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]")))

        driver.find_element_by_xpath("html/body/div/div/div/div[3]/div[3]/div[1]/div[3]/div[3]/div/div[1]/section[3]/div/button[1]").click()
        print "Clicked on publish button"
        
        
        # verifying success message
        
        
        print "Verifying Success message"
        wait.until(EC.visibility_of_element_located((By.XPATH,".//*[@id='content']/div/div/div[2]/div/div/span[2]")))

        headerText=driver.find_element_by_xpath(".//*[@id='content']/div/div/div[2]/div/div/span[2]").text
        print "Message '"+headerText+"' is displayed"
        
        if "You have successfully published" in headerText:
            print("Create a new lesson tab is displayed")
        else:
            print "Success message is not displayed"
            raise Exception

        print "Lesson published"
        
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div/div[3]/div[1]/div/div[2]/div[1]/a").click()
        
        #Verifying created lesson is displayed in list
        
        wait.until(EC.visibility_of_element_located((By.XPATH,"(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]")))

        if driver.find_element_by_xpath("(//tbody/tr/td[2]/a[.='"+lessonName+"'])[1]").is_displayed():
            
            print "\nLesson is displayed in Grid ::"+lessonName
            
        else:
            print "Lesson not displaying in grid"
            raise Exception
        
        driver.find_element_by_xpath(".//*[@id='content']/div/div[3]/div[1]/div/nav/div/div[4]").click()
        
        
    def createCampaignWithLessonTextVideoQuestion(self):
       
        book=xlrd.open_workbook(os.path.join('TestData.xlsx'))
        first_sheet = book.sheet_by_name('CreateCampaigns')
        
        #Campaign Data
        cell1 = first_sheet.cell(89,1)
        campaignTitle = cell1.value
        
        cell1 = first_sheet.cell(90,1)
        campDescription = cell1.value
        
        cell1 = first_sheet.cell(91,1)
        actualSuccessMessage = cell1.value
        
        cell1 = first_sheet.cell(100,1)
        minPassingScore = cell1.value
        
        cell1 = first_sheet.cell(101,1)
        numberOfAttempts = cell1.value
        
        
        #Lesson
        cell1 = first_sheet.cell(93,1)
        lessonName = cell1.value
        
        cell1 = first_sheet.cell(94,1)
        textCard = cell1.value
        
        
        cell1 = first_sheet.cell(95,1)
        videoPath = cell1.value
        
        cell1 = first_sheet.cell(96,1)
        timeToUploadVideo = cell1.value
        
        cell1 = first_sheet.cell(97,1)
        questionCard = cell1.value
        
        cell1 = first_sheet.cell(98,1)
        ans1 = cell1.value
        
        cell1 = first_sheet.cell(99,1)
        ans2 = cell1.value
        
        
        
        try:
            print "\n\n----This test case creates campaign with----\n1. Text, Video and Question lesson\n"
            newobj=CreateCampaignForTxtVidQuesLesson()
            newobj.createLessonTxtVidQue(lessonName, textCard, videoPath, questionCard, ans1, ans2, timeToUploadVideo)
            newobj.createCampaignForLessonTextVideoQuestion(campaignTitle, campDescription, lessonName, actualSuccessMessage, minPassingScore, numberOfAttempts)
            
        finally:
            second_sheet = book.sheet_by_name('Login_Credentials')
            cell = second_sheet.cell(1,1)
            url = cell.value
            driver.get(url)
 