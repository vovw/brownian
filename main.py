from brownian import BrownianMotion, vis_sim 

if __name__ == "__main__":
    robot = BrownianMotion()
    positions = robot.simulate(1000)
    vis_sim(positions)
