import axios from "axios";

export const baseUrl = () => {
    return ('http://0.0.0.0:8000/api/v1')
};

export const decode = (jwt) => {
    const token_parts = jwt.split(/\./);
    return JSON.parse(window.atob(token_parts[1]));
};