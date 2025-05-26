from controller.tradecontroller import TradeController

def main():

    tradecontroller = TradeController()
    tradecontroller.setup()
    running = True

    while(running):
        program_action = tradecontroller.game_loop_step()
        if program_action == "exit":
            running = False

    return

if __name__ == "__main__":
    main()