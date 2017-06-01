from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    def is_going_to_start_state(self,update):
        text = update.message.text
        return text == 'hi'

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'start'

    def is_going_to_state1_2(self, update):
        global text
        text = update.message.text
        return ((text == '剪刀')| (text == '石頭') | (text == '布'))

    def is_going_to_state1_3(self, update):
        global text
        text = update.message.text
        return ((text == '剪刀')| (text == '石頭') | (text == '布'))

    def is_going_to_state1_4(self, update):
        global text
        text = update.message.text
        return ((text == '剪刀')| (text == '石頭') | (text == '布'))

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'method'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'intro'

    def on_enter_start_state(self,update):
        update.message.reply_text("嗨 我是猜拳機器人,要我陪你猜個拳嗎?連續猜贏三次有獎勵喔!\n start-->開始猜拳\n intro-->深入了解我的原理(和獎品) \n method -->相關理論")
        self.advance(update)

    def on_enter_state1(self, update):
        update.message.reply_text("剪刀,石頭......")
        self.advance(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state1_2(self, update):
        global text
        if  text == '剪刀':
            update.message.reply_text("布!")
            update.message.reply_text("你運氣還不錯")
            update.message.reply_text("再來!!!剪刀,石頭......")
            
            self.advance(update)
        elif text == '石頭':
            update.message.reply_text("剪刀!")
            update.message.reply_text("你運氣還不錯")
            update.message.reply_text("再來!!!剪刀,石頭......")
            update.message.text = ''
            self.advance(update)
        elif text == '布':
            update.message.reply_text("石頭!")
            update.message.reply_text("你運氣還不錯")
            update.message.reply_text("再來!!!剪刀,石頭......")
            update.message.text = ''
            self.advance(update)
        

    def on_exit_state1_2(self, update):
        print("......")

    def on_enter_state1_3(self, update):
        global text
        if text == '剪刀':
            update.message.reply_text("布!")
            update.message.reply_text("好了,你下次不可能贏了")
            update.message.reply_text("再來!!!剪刀,石頭......")
            update.message.text = ''
            self.advance(update)
        elif text == '石頭':
            update.message.reply_text("剪刀!")
            update.message.reply_text("好了,你下次不可能贏了")
            update.message.reply_text("再來!!!剪刀,石頭......")
            update.message.text = ''
            self.advance(update)
        elif text == '布':
            update.message.reply_text("石頭!")
            update.message.reply_text("好了,你下次不可能贏了")
            update.message.reply_text("再來!!!剪刀,石頭......")
            update.message.text = ''
            self.advance(update)

    def on_exit_state1_3(self, update):
        print("......")

    def on_enter_state1_4(self, update):
        global text
        if text == '剪刀':
            update.message.reply_text("石頭!")
            update.message.reply_text("遜")
            update.message.reply_text("掰回家練練再來")
            update.message.text = ''
            self.go_back(update)
        elif text == '石頭':
            update.message.reply_text("布!")
            update.message.reply_text("爛")
            update.message.reply_text("掰回家練練再來")
            update.message.text = ''
            self.go_back(update)
        elif text == '布':
            update.message.reply_text("剪刀!")
            update.message.reply_text("嫩")
            update.message.reply_text("掰回家練練再來")
            update.message.text = ''
            self.go_back(update)

    def on_exit_state1_4(self, update):
        print("...")

    def on_enter_state2(self, update):
        update.message.reply_text("Association Rules : http://myweb.fcu.edu.tw/~mhsung/Ecommerce/Data_Mining/Association_Folder/DM_association.htm\n 貝氏定理 : https://taweihuang.hpd.io/2017/03/21/mlbayes/ \n Recurrent Neural Network : http://cpmarkchang.logdown.com/posts/278457-neural-network-recurrent-neural-network")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("我是基於Association rule分析大量的猜拳習慣並以貝氏定理建構recurrent neural networks的猜拳機器人,在交叉驗證下,結果顯示你可以連續猜贏我三次的機率小於ε\n如果你幸運連續猜贏我三次,歡迎來找我,我可以請你吃明天晚餐")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
