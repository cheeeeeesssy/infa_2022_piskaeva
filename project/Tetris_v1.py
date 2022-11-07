
import pygame
import random, time, sys
from pygame.locals import *

fps = 30
window_w, window_h = 800, 600       # Устанавливаем размер окна
block = 20       # Определяем базовый элемент блок размером 20Х20 пикселей
field_w = 20     # определяем ширину игрового поля
field_h = 25     # аналогично редыдущей строке
side_move_time, down_move_time = 0.1, 0.1 # параметры, которые определяют время перемещения объектов при сажатии клавиши "стрелка вниз" (для down_move_time) "Стрелка влево или вправо" (side_move_time)
game_screen_Hpos = int((window_w -field_w*block)/2)      # определяет размещение игрового поля по центру экрана привод к инту для целого результата
game_screen_Vpos = window_h - (field_h * block)          # вертикальное смещение игрового поля

colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))         # синий, зеленый, красный, желтый
lightcolors = ((30, 30, 255), (50, 255, 50), (255, 30, 30), (255, 255, 30))         # светло-синий, светло-зеленый, светло-красный, светло-желтый, нужны для создания "структуры" фигуры, чтобы выглядела объемнее

white, gray, black  = (255, 255, 255), (185, 185, 185), (0, 0, 0)
board_color, background_color, txt_color, title_color, info_color = white, black, white, colors[3], colors[2]

figure_w, figure_h = 5, 5        # определяем ширину и высоту фигур в блоках, они размера 5Х5
        ## Это обусловлено тем, что для перемещения фигуры рядом необходимо пустое пространство в 1 блок, а самая большая длина или ширина фигуры - 4 блкоа для обычной фигуры-палки.
        # ЕСли пространства свободного нет, то фигура не может быть перемещена
        
empty = 'o'
# задаем отрисовку всех фигур, каждая задается, как элемент словаря, для удобства указаны буквы "соответствия типу фигуры" o- пусто x- занято фигурой
figures = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'L': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'J': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}

def pauseScreen():
        ## определяем экран паузы, который вызывается при нажатии на клавишу "P"
        pause = pygame.Surface(( 800, 600))   ## создаем доп поверхность (слой, который размером с наш экран)
        pause.set_alpha(150) # Определяем прозрачность экрана паузы 255 - непрозрачный , 0 -прозрачный полностью
        pause.fill(( 128 , 128,128))  # определяем цвет меню паузы, тут установлен серый                       
        display.blit(pause, (0, 0)) # на игровом экрана отрисовывает поверхность pause в координатах 0,0, размер pause указан выше на 125 строке

def main():
    global fps_clock, display, basic_font, big_font
    pygame.init()
    fps_clock = pygame.time.Clock() ## указываем с какой частотой отрисовки кадров запускать игру
    display = pygame.display.set_mode((window_w, window_h)) # устанавливаем игровое окно
    basic_font = pygame.font.SysFont('arial', 20) # устанавливаем базовый шрифт и его размер
    big_font = pygame.font.SysFont('arial', 45) # устанавливаем шрифт и размер для больших текстов
    pygame.display.set_caption('Тетрис') # Название, создаваемое окна
    showText('Тетрис') # Название игры на экране
    while True: # начинаем игру
        runTetris()  # функция  игры
        pauseScreen() # функция экрана ппаузы
        showText('Конец игры') # вывод текста


def runTetris():
    field = create_field() # для начала создадим игровое поле 
    last_move_down = time.time()  # данные параметры last_... определяют время последнего изменения координаты, необходимо для ускорения перемещения зажатием клавишы
    last_side_move = time.time()
    last_fall = time.time() # определяем для свободного падения объекта без влияния игрока
    going_down = False 
    going_left = False ## три флага going определяют движение фигуры при нажатии на клавиатуру по умолчанию все ложные
    going_right = False
    points = 0 # определяем число очков пользователя
    level, fall_speed = calcSpeed(points) ## определяем уровень сложности и скорость падения фигур от числа очков
    fallingFig = getNewFig() ## получаем новую фигуру, которая будет падать
    nextFig = getNewFig() ## получаем следующую фигуру, которая будет падать

    while True: 
        if fallingFig == None:
            # если нет падающих фигур, генерируем новую
            fallingFig = nextFig # берем фиугуру, что была указана как следуюащя 
            nextFig = getNewFig() # генерим новую следующую фигуру
            last_fall = time.time() 
            if not checkPos(field, fallingFig):
                return # если на игровом поле нет свободного места - игра закончена
        quitGame()
        for event in pygame.event.get(): 
            if event.type == KEYUP: # ТИП СОБЫТИЯ - отпускаем кнопку
                if event.key == K_SPACE: # если отпустили пробел, то пауза и вывод текст  игра приостановлена
                    pauseScreen()
                    showText('Игра приостановлена')
                    last_fall = time.time()
                    last_move_down = time.time()
                    last_side_move = time.time()
                elif event.key == K_LEFT: # если отпустили левую стрелку, то двигать влево не надо
                    going_left = False
                elif event.key == K_RIGHT: # если отпустили правую, то двигать вправо не надо
                    going_right = False
                elif event.key == K_DOWN:  # если отпустили правую, то ускоренно двигать вниз не надо
                    going_down = False

            elif event.type == KEYDOWN:
                # ТИП СОБЫТИЯ - нажали на кнопку, но не отпускали ее именно нажали
                if event.key == K_LEFT and checkPos(field, fallingFig, adjX=-1): # если можно двигать влево, то смещаем координату х на один, ставим флаг двигать влево
                    fallingFig['x'] -= 1
                    going_left = True
                    going_right = False # cнимаем флаг двигать вправо, потому что до этого могли двигать направо
                    last_side_move = time.time() 

                elif event.key == K_RIGHT and checkPos(field, fallingFig, adjX=1):
                    fallingFig['x'] += 1 # если можно двигать вправо, то двигаем 
                    going_right = True
                    going_left = False
                    last_side_move = time.time()

                # поворачиваем фигуру, если есть место
                elif event.key == K_UP:
                    fallingFig['rotation'] = (fallingFig['rotation'] + 1) % len(figures[fallingFig['shape']]) # % дает остаток от делениЯ, таким образом мы будем всегда ходить по существующим вариантам и ошибок не возникнет
                    if not checkPos(field, fallingFig): # если вращение приводит к выходу за границы или попадаем на фигуру, то откатываем назад
                        fallingFig['rotation'] = (fallingFig['rotation'] - 1) % len(figures[fallingFig['shape']])

                # ускоряем падение фигуры
                elif event.key == K_DOWN:
                    going_down = True
                    if checkPos(field, fallingFig, adjY=1): # можно падать, то падаем на 1 клетку ниже
                        fallingFig['y'] += 1
                    last_move_down = time.time()

                # мгновенный сброс вниз
                elif event.key == K_RETURN: # если нажать Enter, то полетит сразу в самый низ, который доступен
                    going_down = False
                    going_left = False
                    going_right = False
                    for i in range(1, field_h):
                        if not checkPos(field, fallingFig, adjY=i):  # падаем, пока можнно, если нельзя, то останавливаемся и остаемся на позции выше той, куда попали на 1
                            break 
                    fallingFig['y'] += i - 1

        # управление падением фигуры при удержании клавиш
        if (going_left or going_right) and time.time() - last_side_move > side_move_time:  # смотрим разницу между текущим временем time.time() и временем предыдущего смещения, если оно больше, чем время, определяющее боковое смещение, значит клавиша зажата
            if going_left and checkPos(field, fallingFig, adjX=-1): # в случае возможного смещения влево, смещаемся влево
                fallingFig['x'] -= 1
            elif going_right and checkPos(field, fallingFig, adjX=1): # можем уйти вправо- смещаемся вправо
                fallingFig['x'] += 1
            last_side_move = time.time() # запоминаем время смещения по горизонтали

        if going_down and time.time() - last_move_down > down_move_time and checkPos(field, fallingFig, adjY=1): # если разность больше установленного времени, то клавиша зажата
            fallingFig['y'] += 1
            last_move_down = time.time()


        if time.time() - last_fall > fall_speed: #  если разность больше, чем скорость падения, то
            if not checkPos(field, fallingFig, adjY=1): # проверка "приземления" фигуры
                addTofield(field, fallingFig) # фигура приземлилась, добавляем ее в содержимое игрового поля
                points += clearCompleted(field) # наше число очков опредляется как число удаленных линий * 100
                level, fall_speed = calcSpeed(points) # увеличиваем скорость при необходимости
                fallingFig = None  # устанавливаем, что пока что нет падающих фигур
            else: # фигура пока не приземлилась, продолжаем движение вниз
                fallingFig['y'] += 1
                last_fall = time.time()

        # рисуем окно игры со всеми надписями
        display.fill(background_color) # при объявлении указали,что цвет черный
        drawTitle() # рисуем заголовок в окне игры
        gamefield(field) # отрисовка игрового поля
        drawInfo(points, level) # указываем вспомогательную информацию
        drawnextFig(nextFig) # отрисовываем след фигурку
        if fallingFig != None:
            drawFig(fallingFig) # если что-то падает, то надо это отрисовать 
        pygame.display.update() # обновляем экран
        fps_clock.tick(fps) # устанавливаем с какой частотой кадров запускаться программе


def txtObjects(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()


def stop_game():
    pygame.quit()
    sys.exit()


def checkKeys():
    quitGame()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None


def showText(text):
    titleSurf, titleRect = txtObjects(text, big_font, title_color)
    titleRect.center = (int(window_w / 2) , int(window_h / 2) )
    display.blit(titleSurf, titleRect)
   
    pressKeySurf, pressKeyRect = txtObjects('Нажмите любую клавишу для продолжения', basic_font, title_color)
    pressKeyRect.center = (int(window_w / 2), int(window_h / 2) + 100)
    display.blit(pressKeySurf, pressKeyRect)

    while checkKeys() == None:
        pygame.display.update()
        fps_clock.tick()


def quitGame():
    for event in pygame.event.get(QUIT): # проверка всех событий, приводящих к выходу из игры
        stop_game() 
    for event in pygame.event.get(KEYUP): 
        if event.key == K_ESCAPE: # проверяем нажатие клавишы, если нажали эскейп, то выходим из игры
            stop_game() 
        pygame.event.post(event)  # отрпавляем наше событие программе


def calcSpeed(points):
    # вычисляем уровень сложности
    level = int(points / 1000) + 1 # делим на 1000, так как прибавляем стандартно по 100 очков
    fall_speed = 0.5 - (level * 0.05) # cначала будет медленно падать, потом скорость возрастет
    return level, fall_speed 

def getNewFig():
    # возвращает новую фигуру со случайным цветом и углом поворота
    shape = random.choice(list(figures.keys())) ## ,берет случайную фигуру из нашего перечня figures shape - тип фигуры в нашем "словаре фигур", например S,Z,J,L 
    newFigure = {'shape': shape,
                'rotation': random.randint(0, len(figures[shape]) - 1), # получаем поворот от 0 до числа вариантов поворотов -1
                'x': int(field_w / 2) - int(figure_w / 2), # кидаем в ЦЕНТР экрана и смещаем так,чтобы центр фиугры стал по центру экрана
                'y': 0, # положение откуда падает фигура по вертикалии - самый верх, учитываем, что у фигуры еще есть мнимая область границ
                'color': random.randint(0, len(colors)-1)} # даем фигуре случайный цвет из нашего списка 
    return newFigure


def addTofield(field, fig):
    for x in range(figure_w):
        for y in range(figure_h):
            if figures[fig['shape']][fig['rotation']][y][x] != empty:
                field[x + fig['x']][y + fig['y']] = fig['color'] # Закрашиваем поле там, где расположены x у фигуры


def create_field():
    # создаем пустое игровое поле
    field = []
    for i in range(field_w):
        # создаем поле: для каждого столбца, шириной в клетку поля добавляем по строчке высотой в клетку поля
        field.append([empty] * field_h) # empty - это наш элемент o, который был объявлен ранее
        # получили пустое поле вида 
        #                           ooooo
        #                           ooooo
        #                           ooooo
        #                           ooooo 
        # и так далее    
    return field


def infield(x, y):
    return x >= 0 and x < field_w and y < field_h
    


def checkPos(field, fig, adjX=0, adjY=0):
    # проверяет, находится ли фигура в границах игрового поля, не сталкиваясь с другими фигурами
    for x in range(figure_w): # для каждого квадратика в ширине фигуры
        for y in range(figure_h): # для каждого квадратика в высоте фигуры 
            if figures[fig['shape']][fig['rotation']][y][x] == empty: # проверка: квадратик в отрисовке фигуры пустой, если да, то смотрим следующий
                continue
            if not infield(x + fig['x'] + adjX, y + fig['y'] + adjY): # проверка присутствия фигуры внутри игрового поляес, если вышли за границы, то такая позиция недоступна
                return False
            if field[x + fig['x'] + adjX][y + fig['y'] + adjY] != empty: # если поле, куда хотим встать не пустое, т.е. не содержит символ o, то позиция недоступна
                return False
    return True

def isCompleted(field, y):
    # проверяем наличие полностью заполненных рядов
    for x in range(field_w):
        if field[x][y] == empty: # если где-то пусто, то ряд не заполнен
            return False
    return True


def clearCompleted(field):
    # Удаление заполенных рядов и сдвиг верхних рядов вниз
    removed_lines = 0
    y = field_h - 1 # последнее поле
    while y >= 0:
        if isCompleted(field, y): # проверяем заполнен ли последний ряд
           for pushDownY in range(y, 0, -1): # смотрим с последнего ряда до первого
                for x in range(field_w):
                    field[x][pushDownY] = field[x][pushDownY-1] # заменяем ряды, путем смещения их вниз на 1
           for x in range(field_w):
                field[x][0] = empty # заполняем самый верхний ряд пустотой
           removed_lines += 100 # увеличиваем наши баллы на 100
        else:
            break
    return removed_lines


def convertCoords(block_x, block_y):
    return (game_screen_Hpos + (block_x * block)), (game_screen_Vpos+ (block_y * block)) # возвращаем координаты пикселей блока на сцене


def drawBlock(block_x, block_y, color, pixelx=None, pixely=None):
    #отрисовка квадратных блоков, из которых состоят фигуры
    if color == empty:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convertCoords(block_x, block_y)
    # следующие три функции отрисовывают блок ( квадратик 20Х20), в котором попиксельно отрисовывается два прямоугольника разных цветов и кружочек, если цвет черный, то ничего не будет видно, а иначе будет рисоваться фиурка
    pygame.draw.rect(display, colors[color], (pixelx + 1, pixely + 1, block - 1, block - 1), 0, 3) # закрашиваем пиксели поля, если фигурки там нет, то цвет будет черный
    pygame.draw.rect(display, lightcolors[color], (pixelx + 1, pixely + 1, block - 4, block - 4), 0, 3) # если цвет не черный, то будет получаться часть фигурки 

    pygame.draw.circle(display, colors[color], (pixelx + block / 2, pixely + block / 2), 5) # доотрисовка фигурки, добавление на нее кружочка
    
def gamefield(field):
    # граница игрового поля
    pygame.draw.rect(display, board_color, (game_screen_Hpos, game_screen_Vpos, (field_w * block) , (field_h * block)), 2) # параметры задают рамку поля, кроме того, толщина рамки - последний параметр и равна 5

    # фон игрового поля
    # pygame.draw.rect(display, background_color, (game_screen_Hpos, game_screen_Vpos, block * field_w, block * field_h-10))
    for x in range(field_w):
        for y in range(field_h):
            pygame.draw.rect(display, white, (game_screen_Hpos+1+x*field_w,game_screen_Vpos+ y*field_h-1,field_w,field_h), 1) # ОТРИСОВКА СЕТКИ 
            drawBlock(x, y, field[x][y]) # fiekd [x][y] содержит цвет фигуры, находящейся в этой позиции

def drawTitle():
    titleSurf = big_font.render('Тетрис', True, title_color)
    titleRect = titleSurf.get_rect() # прямоугольник, ограничивающий текст
    titleRect.topleft = (window_w /2 - int(titleSurf.get_width()/2), 30) # указываем позицию заголовка
    display.blit(titleSurf, titleRect) # добавляем наш текст на окно с размерами прямоугольника
    

def drawInfo(points, level):

    pointsSurf = basic_font.render(f'Очки: {points}', True, txt_color)  # указывается поверхность, на которой будет текст, второй параметр - сглаживание (true - значит есть сглаживание), третий - цвет текста
    pointsRect = pointsSurf.get_rect()
    pointsRect.topleft = (50, 180) # координаты информации о баллах
    display.blit(pointsSurf, pointsRect) # привязываем поверхность к нашему окну с ограничивающим прямоуголником pointsRect

    levelSurf = basic_font.render(f'Уровень: {level}', True, txt_color)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (50, 200)
    display.blit(levelSurf, levelRect)

    pausebSurf = basic_font.render('Пауза: пробел', True, info_color)
    pausebRect = pausebSurf.get_rect()
    pausebRect.topleft = (50, 220)
    display.blit(pausebSurf, pausebRect)
    
    escbSurf = basic_font.render('Выход: Esc', True, info_color)
    escbRect = escbSurf.get_rect()
    escbRect.topleft = (50, 240)
    display.blit(escbSurf, escbRect)

def drawFig(fig, pixelx=None, pixely=None):
    figToDraw = figures[fig['shape']][fig['rotation']]
    if pixelx == None and pixely == None:    
        pixelx, pixely = convertCoords(fig['x'], fig['y'])

    #отрисовка элементов фигур
    for x in range(figure_w):
        for y in range(figure_h):
            if figToDraw[y][x] != empty:
                drawBlock(None, None, fig['color'], pixelx + (x * block), pixely + (y * block))


def drawnextFig(fig):  # превью следующей фигуры
    nextSurf = basic_font.render('Следующая:', True, txt_color)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (window_w - 150, 180)
    display.blit(nextSurf, nextRect)
    drawFig(fig, pixelx=window_w-150, pixely=200) # рисуем фигурку в кординатах window_w-150 ,200


if __name__ == '__main__':
    main()
