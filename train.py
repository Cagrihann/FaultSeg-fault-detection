from ultralytics import YOLO

if __name__ == "__main__": #multiprocessing'de sonsuz döngüyü engeller           RuntimeError:
    model = YOLO("yolo11n.pt")                                                #         An attempt has been made to start a new process before the
    train_results = model.train(                                              #         current process has finished its bootstrapping phase.
        data="data/data.yaml", 
        epochs=300,  
        imgsz=640,  
        device="cuda:0",                                                      #         This probably means that you are not using fork to start your
                                                                              #         child processes and you have forgotten to use the proper idiom
                                                                              #         in the main module: 
                                                                              #             if __name__ == '__main__':
                                                                              #                 freeze_support()
                                                                              #                 ...

                                                                              #         The "freeze_support()" line can be omitted if the program
                                                                              #         is not going to be frozen to produce an executable.

    )
