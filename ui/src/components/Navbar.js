import styles from "../css/navbar.module.css";
const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className={styles.navContent}>
                <div className="navbar-brand">Python-Help</div>
                <input className="form-control" type="search" placeholder="Search"/>
                <button className="btn btn-primary">Help</button>
            </div>
        </nav>
    );
}

export default Navbar;