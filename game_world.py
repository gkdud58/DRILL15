world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
        if o in pairs[2]:
            pairs[2].remove(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()

def collide(a, b, c):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    left_c, bottom_c, right_c, top_c = c.get_bb()
    
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    if left_c > right_b: return False
    if right_c < left_b: return False
    if top_c < bottom_b: return False
    if bottom_c > top_b: return False
        
    if left_a > right_c: return False
    if right_a < left_c: return False
    if top_a < bottom_c: return False
    if bottom_a > top_c: return False
        
    return True


collision_pairs = {}

def add_collision_pairs(group, a, b,c):
    if group not in collision_pairs:
        collision_pairs[group] = [[],[],[]]
    if a: collision_pairs[group][0].append(a)
    if b: collision_pairs[group][1].append(b)
    if c: collision_pairs[group][2].append(c)

def handle_collision():
    for group, pairs in collision_pairs.items():
        for a in pairs[0][:][:]:  # 순회 중 리스트 변경 방지를 위해 복사본 사용
            for b in pairs[1][:][:]:
                for c in pairs[2][:][:]:
                   if collide(a, b, c):
                        a.handle_collision(group, b)
                        b.handle_collision(group, c)
                        c.handle_collision(group,a)

def remove_collision_pairs(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs.remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
        if o in pairs[2]:
            pairs.remove(o)

def clear():
    for layer in world:
        layer.clear()

