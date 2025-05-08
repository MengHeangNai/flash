export function setItem(key: string, value: unknown) {
    try {
        window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
        console.log(error);
    }
}

export function getItem(key: string) {
    try {
        const item = window.localStorage.getItem(key);
        return item ? JSON.parse(item) : undefined;
    } catch (error) {
        console.log(error);
    }
}

export function removeItem(key: string) {
    try {
        window.localStorage.removeItem(key);
    } catch (error) {
        console.log(error);
    }
}

export function clear() {
    try {
        window.localStorage.clear();
    } catch (error) {
        console.log(error);
    }
}

export function getAllKeys() {
    try {
        return Object.keys(window.localStorage);
    } catch (error) {
        console.log(error);
    }
}

export function getAllItems() {
    try {
        const items: Record<string, unknown> = {};
        const keys = Object.keys(window.localStorage);
        keys.forEach((key) => {
            items[key] = window.localStorage.getItem(key);
        });
        return items;
    } catch (error) {
        console.log(error);
    }
}

// sessionStorage
export function setSessionItem(key: string, value: unknown) {
    try {
        window.sessionStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
        console.log(error);
    }
}

export function getSessionItem(key: string) {
    try {
        const item = window.sessionStorage.getItem(key);
        return item ? JSON.parse(item) : undefined;
    } catch (error) {
        console.log(error);
    }
}

export function removeSessionItem(key: string) {
    try {
        window.sessionStorage.removeItem(key);
    } catch (error) {
        console.log(error);
    }
}

export function clearSession() {
    try {
        window.sessionStorage.clear();
    } catch (error) {
        console.log(error);
    }
}

export function getAllSessionKeys() {
    try {
        return Object.keys(window.sessionStorage);
    } catch (error) {
        console.log(error);
    }
}

export function getAllSessionItems() {
    try {
        const items: Record<string, unknown> = {};
        const keys = Object.keys(window.sessionStorage);
        keys.forEach((key) => {
            items[key] = window.sessionStorage.getItem(key);
        });
        return items;
    } catch (error) {
        console.log(error);
    }
}

export function clearAllStorage() {
    try {
        clear();
        clearSession();
    } catch (error) {
        console.log(error);
    }
}

export function getAllStorage() {
    try {
        const localStorageItems = getAllItems();
        const sessionStorageItems = getAllSessionItems();
        return { localStorageItems, sessionStorageItems };
    } catch (error) {
        console.log(error);
    }
}

export function getAllStorageKeys() {
    try {
        const localStorageKeys = getAllKeys();
        const sessionStorageKeys = getAllSessionKeys();
        return { localStorageKeys, sessionStorageKeys };
    } catch (error) {
        console.log(error);
    }
}

export function getAllStorageItems() {
    try {
        const localStorageItems = getAllItems();
        const sessionStorageItems = getAllSessionItems();
        return { ...localStorageItems, ...sessionStorageItems };
    } catch (error) {
        console.log(error);
    }
}
