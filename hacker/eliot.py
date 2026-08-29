import pygame
import random
import math

pygame.init()

WIDTH = 1100
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GTA 6 MINI")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 30)
big_font = pygame.font.Font(None, 55)

# ---------------- PLAYER ----------------

player = pygame.Rect(500, 330, 30, 30)

health = 100
money = 500
wanted = 0
score = 0

speed = 5

# ---------------- CAR ----------------

car = pygame.Rect(650, 300, 80, 45)

in_car = False

# ---------------- ENEMY ----------------

enemies = []

for i in range(5):
    enemy = pygame.Rect(
        random.randint(100, 950),
        random.randint(100, 600),
        30,
        30
    )
    enemies.append(enemy)

# ---------------- BULLETS ----------------

bullets = []

# ---------------- MISSION ----------------

mission = pygame.Rect(900, 100, 40, 40)
mission_done = False

# ---------------- GAME ----------------

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # SHOOT
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                px = player.centerx
                py = player.centery

                dx = mouse_x - px
                dy = mouse_y - py

                distance = math.sqrt(dx * dx + dy * dy)

                if distance != 0:

                    dx /= distance
                    dy /= distance

                    bullets.append(
                        [px, py, dx * 10, dy * 10]
                    )

    keys = pygame.key.get_pressed()

    # ---------------- MOVEMENT ----------------

    dx = 0
    dy = 0

    if keys[pygame.K_w]:
        dy -= speed

    if keys[pygame.K_s]:
        dy += speed

    if keys[pygame.K_a]:
        dx -= speed

    if keys[pygame.K_d]:
        dx += speed

    # ---------------- CAR ----------------

    if keys[pygame.K_e]:

        if player.colliderect(car):
            in_car = True

    if keys[pygame.K_q]:

        if in_car:
            in_car = False

    if in_car:

        car.x += dx
        car.y += dy

        player.center = car.center

    else:

        player.x += dx
        player.y += dy

    # ---------------- SCREEN LIMIT ----------------

    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    car.x = max(0, min(WIDTH - car.width, car.x))
    car.y = max(0, min(HEIGHT - car.height, car.y))

    # ---------------- BULLETS ----------------

    for bullet in bullets[:]:

        bullet[0] += bullet[2]
        bullet[1] += bullet[3]

        if (
            bullet[0] < 0
            or bullet[0] > WIDTH
            or bullet[1] < 0
            or bullet[1] > HEIGHT
        ):
            bullets.remove(bullet)
            continue

        bullet_rect = pygame.Rect(
            bullet[0],
            bullet[1],
            8,
            8
        )

        for enemy in enemies[:]:

            if bullet_rect.colliderect(enemy):

                enemies.remove(enemy)

                score += 100
                wanted = min(5, wanted + 1)

                bullets.remove(bullet)

                break

    # ---------------- ENEMIES ----------------

    for enemy in enemies:

        if enemy.x < player.x:
            enemy.x += 1

        if enemy.x > player.x:
            enemy.x -= 1

        if enemy.y < player.y:
            enemy.y += 1

        if enemy.y > player.y:
            enemy.y -= 1

        if enemy.colliderect(player):

            health -= 1

    # ---------------- MISSION ----------------

    if player.colliderect(mission) and not mission_done:

        mission_done = True

        money += 1000
        score += 500

    # ---------------- DRAW ----------------

    screen.fill((45, 140, 65))

    # roads

    pygame.draw.rect(
        screen,
        (70, 70, 70),
        (0, 250, WIDTH, 130)
    )

    pygame.draw.rect(
        screen,
        (70, 70, 70),
        (400, 0, 130, HEIGHT)
    )

    # road lines

    for x in range(0, WIDTH, 80):

        pygame.draw.rect(
            screen,
            (230, 210, 50),
            (x, 310, 40, 5)
        )

    for y in range(0, HEIGHT, 80):

        pygame.draw.rect(
            screen,
            (230, 210, 50),
            (462, y, 5, 40)
        )

    # buildings

    buildings = [
        (50, 50, 180, 140),
        (650, 50, 200, 140),
        (700, 450, 250, 150),
        (70, 470, 200, 120)
    ]

    for building in buildings:

        pygame.draw.rect(
            screen,
            (35, 35, 40),
            building
        )

    # mission

    if not mission_done:

        pygame.draw.rect(
            screen,
            (255, 210, 0),
            mission
        )

    # car

    pygame.draw.rect(
        screen,
        (220, 40, 40),
        car
    )

    pygame.draw.rect(
        screen,
        (30, 120, 200),
        (car.x + 10, car.y + 8, 25, 18)
    )

    pygame.draw.rect(
        screen,
        (30, 120, 200),
        (car.x + 45, car.y + 8, 25, 18)
    )

    # player

    if not in_car:

        pygame.draw.rect(
            screen,
            (40, 100, 255),
            player
        )

    # enemies

    for enemy in enemies:

        pygame.draw.rect(
            screen,
            (30, 30, 30),
            enemy
        )

    # bullets

    for bullet in bullets:

        pygame.draw.circle(
            screen,
            (255, 230, 50),
            (int(bullet[0]), int(bullet[1])),
            5
        )

    # ---------------- HUD ----------------

    hud = font.render(
        f"💰 ${money}    ❤️ {health}    ⭐ Wanted: {wanted}    🏆 {score}",
        True,
        (255, 255, 255)
    )

    screen.blit(hud, (20, 20))

    controls = font.render(
        "WASD = Move | E = Enter Car | Q = Exit | LEFT CLICK = Shoot",
        True,
        (255, 255, 255)
    )

    screen.blit(controls, (20, HEIGHT - 40))

    if mission_done:

        text = big_font.render(
            "MISSION COMPLETE! +$1000",
            True,
            (255, 220, 40)
        )

        screen.blit(
            text,
            (WIDTH // 2 - 250, 80)
        )

    # ---------------- GAME OVER ----------------

    if health <= 0:

        screen.fill((20, 20, 20))

        text = big_font.render(
            "GAME OVER",
            True,
            (255, 50, 50)
        )

        screen.blit(
            text,
            (WIDTH // 2 - 130, HEIGHT // 2)
        )

        pygame.display.flip()

        pygame.time.wait(3000)

        running = False

    pygame.display.flip()

pygame.quit()