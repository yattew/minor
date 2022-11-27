import { useContext } from "react";
import LearningModeContext, { modes } from "../Contexts";
import styles from "../css/navbar.module.css";
import Search from "./Search";
const Navbar = () => {
    const { mode, setMode, modes } = useContext(LearningModeContext);
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className={styles.navContent}>
                <div className={styles.leftContent}>
                    <div className="navbar-brand">Python-Help</div>
                </div>
                <Search />

                <div className={styles.rightContent}>
                    <ul className="nav navbar-nav">
                        <li className="nav-item dropdown">
                            <span
                                className="nav-link dropdown-toggle"
                                data-bs-toggle="dropdown"
                                style={{
                                    "cursor":"pointer"
                                }}
                            >
                                {mode.toUpperCase()}
                            </span>
                            <div className="dropdown-menu dropdown-menu-end">
                                {
                                    (() => {
                                        let arr = [];
                                        for (let mode in modes) {
                                            arr.push(
                                                <span
                                                    className="dropdown-item"
                                                    key={mode}
                                                    style={{
                                                        "cursor":"pointer"
                                                    }}
                                                    onClick={() => {
                                                        setMode(mode);
                                                    }}
                                                >
                                                    {mode.toUpperCase()}
                                                </span>
                                            )
                                        }
                                        return arr;
                                    })()
                                }
                            </div>
                        </li>
                    </ul>
                    <button className="btn btn-primary">Help</button>
                </div>
            </div>


        </nav>
    );
}

export default Navbar;